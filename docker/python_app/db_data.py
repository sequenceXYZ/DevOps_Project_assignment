import db_connect as db


def get_all_instances():
    instance_list = []
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT name, ami, region FROM instances")
            for instance in cursor.fetchall():
                instance_dict = {
                    'name': instance[0],
                    'ami': instance[1],
                    'region': instance[2]
                }
                instance_list.append(instance_dict)
    return instance_list


def create_new_instance(instance):
    existing_instance = get_one_instance(instance['name'])
    if existing_instance:
        return {'error': f"Instance with name {instance['name']} already exists"}, 409

    with db.create_connection() as connection:
        with connection.cursor() as cursor:
            query = "INSERT INTO instances (name, ami, region) VALUES (%s, %s, %s);"
            values = (instance['name'], instance['ami'], instance['region'])
            cursor.execute(query, values)
            connection.commit()
    return instance, 201


def get_one_instance(name):
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT name, ami, region FROM instances WHERE name ='" + name + "'")
            instance = cursor.fetchone()
            if instance is not None:
                return {
                    'name': instance[0],
                    'ami': instance[1],
                    'region': instance[2]
                }
            else:
                return None


def delete_instance(name):
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            delete_query = "DELETE FROM instances WHERE name ='" + name + "'"
            cursor.execute(delete_query)
            conn.commit()
            return cursor.rowcount


def update_instance(name, instance):
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            update_query = "UPDATE instances SET ami = %s, region = %s WHERE name = %s"
            values = (instance['ami'], instance['region'], name)
            cursor.execute(update_query, values)
            conn.commit()
        return instance

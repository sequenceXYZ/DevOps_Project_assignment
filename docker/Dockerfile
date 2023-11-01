# Use the slim variant of the Python 3.9 image
FROM python:3.9-slim

# Set the working directory for the application
WORKDIR /app

# Expose the port the Flask app will run on
EXPOSE 8000

# Copy application files to the working directory
COPY python_app /app

# Install dependencies
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Start the Flask application
CMD ["python", "app.py"]
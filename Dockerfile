FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the Flask app code into the container
COPY app app

# Copy the NGINX configuration file into the container
COPY nginx.conf /etc/nginx/nginx.conf

# Expose the port on which the app will run
EXPOSE 8080

# Start the app with gunicorn and nginx
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:8080", "app.main:app"]
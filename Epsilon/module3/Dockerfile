# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5003

# Run the app
CMD ["python", "app.py"]

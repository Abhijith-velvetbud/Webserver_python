# Use a lightweight Python base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port your application listens on (adjust if needed)
EXPOSE 8082

# Command to run the application
CMD ["python", "app.py"]

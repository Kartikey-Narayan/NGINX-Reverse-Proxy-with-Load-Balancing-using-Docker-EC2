# Use a minimal official Python image (small and efficient)
FROM python:alpine3.21

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install dependencies listed in requirements.txt without caching to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 3001 (Flask default)
EXPOSE 3001

# Define the command to run the Flask app
CMD ["python", "app.py"]
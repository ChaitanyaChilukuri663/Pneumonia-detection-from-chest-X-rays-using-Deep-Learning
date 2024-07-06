# Use Python 3.10 base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port on which your Flask app runs
EXPOSE 5000

# Command to run your Flask application
CMD ["python", "app.py"]

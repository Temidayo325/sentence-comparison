# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application directory into the container
COPY . .

# Expose the port that the FastAPI application will run on
EXPOSE 5000

# Run the FastAPI application using uvicorn
CMD ["uvicorn", "router.main:app", "--host", "0.0.0.0", "--port", "5000"]

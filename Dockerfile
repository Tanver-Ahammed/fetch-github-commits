# Use an official Python runtime as a parent image
FROM python:3.9-alpine3.21

# Set the working directory in the container
WORKDIR /app

# Copy the script into the container
COPY fetch_commits.py .

# Install dependencies
RUN pip install requests

# Run the script
CMD ["python", "fetch_commits.py"]

# Use the official Python 3.12 Alpine image
FROM python:3.12-alpine

# Set the working directory
WORKDIR /app

# Install necessary dependencies
RUN apk add python3-dev gcc libc-dev libffi-dev

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8080

# Use Uvicorn to run the FastAPI app with --host 0.0.0.0 to allow external access
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
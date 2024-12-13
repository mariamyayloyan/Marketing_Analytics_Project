# Base Image
FROM python:3.10-slim-bullseye

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev libfreetype6-dev libpng-dev libjpeg-dev \
    libblas-dev liblapack-dev gfortran \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /etl

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy application code
COPY . .

# Expose the application port
EXPOSE 3000

# Define default command
CMD ["python", "etl.py"]

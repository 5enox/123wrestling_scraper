# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install SQL and Playwright dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    libffi-dev \
    libxslt-dev \
    libxml2-dev \
    libjpeg-dev \
    libpng-dev \
    libssl-dev \
    libfontconfig \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libgtk-3-0 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Set the entrypoint command to launch main.py
CMD ["python", "main.py"]

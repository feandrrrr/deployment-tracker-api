# Use a lightweight Python image as the base environment
FROM python:3.12-slim

# Set /app as the working directory inside the container
WORKDIR /app

# Copy the dependency file first
COPY requirements.txt .

# Install the Python packages required by the application
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . .

# Port 8000
EXPOSE 8000

# Start the FastAPI application when the container runs
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
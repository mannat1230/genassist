# Base image
FROM python:3.10

# Set work directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Default command for FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
FROM python:3.11-slim

# Create non-root user
RUN useradd -m appuser

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install only build essentials
RUN apt-get update && apt-get install -y \
    gcc g++ libffi-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy only necessary source code
COPY data ./data
COPY src ./src
COPY main.py .
COPY .env .env
COPY templates ./templates
COPY static ./static

# Use non-root user
USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


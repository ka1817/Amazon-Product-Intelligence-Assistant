# ----------------------
# Stage 1: Build stage
# ----------------------
FROM python:3.11-slim AS builder

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements and build Python wheels
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt

# ------------------------
# Stage 2: Production stage
# ------------------------
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy wheels and requirements
COPY --from=builder /wheels /wheels
COPY --from=builder /app/requirements.txt .

# Install Python packages from wheels
RUN pip install --no-cache-dir /wheels/*

# Copy source code
COPY . .

# Expose FastAPI default port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# =========================================
# Stage 1: Builder
# =========================================
FROM python:3.10-slim AS builder

WORKDIR /app

# Install system dependencies (Graphviz)
RUN apt-get update && apt-get install -y graphviz

# Install Python dependencies
RUN pip install --no-cache-dir flask graphviz

# Copy project files
COPY . .

# =========================================
# Stage 2: Final Image
# =========================================
FROM python:3.10-slim

WORKDIR /app

# Install runtime dependency (Graphviz only)
RUN apt-get update && apt-get install -y graphviz

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy project files
COPY . .

# Expose port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]
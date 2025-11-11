# Dockerfile
FROM python:3.10-slim

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Force stdout/stderr to be unbuffered
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    apt-get clean

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project code
COPY . .

# Collect static files (optional: skip in dev)
RUN python manage.py collectstatic --noinput || true

# Expose port
EXPOSE 8000

# Run app with gunicorn (production style)
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]

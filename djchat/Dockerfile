# djchat/Dockerfile (dev)
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# system deps (if you need mysqlclient or others, add build deps here)
RUN apt-get update && apt-get install -y build-essential libpq-dev gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy project (copying only djchat dir contents)
COPY . /app

# Expose port used by Django dev server
EXPOSE 8000

# Use runserver for dev. In production use gunicorn (see prod example below)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

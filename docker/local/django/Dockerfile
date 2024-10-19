FROM python:3.12.7-slim

# Set the application home directory
ENV APP_HOME=/app

# Create application directories
RUN mkdir -p $APP_HOME/staticfiles

# Set the working directory
WORKDIR $APP_HOME

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install necessary packages
RUN apt-get update && \
    apt-get install -y build-essential \
                       libpq-dev \
                       gettext \
                       netcat-openbsd \
                       gcc \
                       postgresql && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip3 install --upgrade pip

# Copy requirements.txt and install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Copy entrypoint and make it executable
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint && \
    chmod +x /entrypoint

# Copy start script and make it executable
COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start && \
    chmod +x /start

COPY ./docker/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker && chmod +x /start-celeryworker

COPY ./docker/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower && chmod +x /start-flower

# Set the entrypoint
ENTRYPOINT ["/entrypoint"]

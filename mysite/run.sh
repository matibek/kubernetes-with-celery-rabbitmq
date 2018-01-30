#!/bin/bash
# This will be called from docker entry point
set -ex


if [ "$WORKER" = "true" ]; then
    echo "Running worker server..."
    exec celery -A mysite worker --loglevel=INFO -Q short_job
    exit 0
fi

echo "Running web server..."
exec gunicorn -b :8000 mysite.wsgi
FROM python:3.11

### Requirements for Weasyprint
RUN apt-get update && apt-get install -y libcairo2 \
  gunicorn \
  libpango-1.0-0 \
  libpangocairo-1.0-0 \
  libgdk-pixbuf2.0-0 \
  libffi-dev \
  shared-mime-info \
  ### Added for use exec command (open container console) in Heroku
  openssh-server \
  ###
  && rm -rf /var/lib/apt/lists/*

### Added for use exec command (open container console) in Heroku
RUN rm /bin/sh \
  && ln -s /bin/bash /bin/sh \
  && mkdir -p /app/.profile.d/ \
  && printf '#!/usr/bin/env bash\n\nset +o posix\n\n[ -z "$SSH_CLIENT" ] && source <(curl --fail --retry 7 -sSL "$HEROKU_EXEC_URL")\n' > /app/.profile.d/heroku-exec.sh \
  && chmod +x /app/.profile.d/heroku-exec.sh
###

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install whitenoise

COPY . /app

COPY docker-entrypoint.sh /docker-entrypoint.sh

EXPOSE 8000

CMD ["/docker-entrypoint.sh"]

# Create necessary directories
RUN mkdir -p staticfiles

# Copy static files
# COPY static/ /app/static/

# Collect static files
RUN python manage.py collectstatic --noinput --clear
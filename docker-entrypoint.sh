#!/bin/bash

set -e

action=$1

# cd app

if [ "$action" = "migrations" ]
then
  sleep 30
  echo "Running migrations"
  python manage.py migrate --noinput

elif [ "$action" = "createsuperuser" ]
then
  sleep 40
  python manage.py createsuperuser --noinput

else
  sleep 10
  echo "Running django application"
  python manage.py collectstatic --noinput
  python manage.py runserver 0.0.0.0:8000
fi

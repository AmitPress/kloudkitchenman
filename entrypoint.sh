#!/bin/bash

# check for env vars
if [ -f .env ]; then
    set -a
    source .env
    set +a
fi

sleep 10
python manage.py makemigrations
python manage.py migrate
python manage.py autocreatesuperuser --username $SUPERUSERNAME --email $SUPERUSEREMAIL --password $SUPERUSERPASSWORD
python manage.py runserver 0.0.0.0:$APP_CONTAINER_PORT
#!/bin/bash

# check for env vars
if [ -f .env ]; then
    set -a
    source .env
    set +a
fi


python manage.py makemigrations
python manage.py migrate
python manage.py autocreatesuperuser --username $SUPERUSERNAME --email $SUPERUSEREMAIL --password $SUPERUSERPASSWORD
python manage.py runserver 0.0.0.0:$APP_CONTAINER_PORT
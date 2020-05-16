#!/bin/sh

python manage.py migrate
python manage.py flush --no-input
python manage.py create_user -u $DJANGO_ADMIN -e $DJANGO_EMAIL -p $DJANGO_PASSWORD

exec "$@"
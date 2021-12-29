#!/bin/sh
python ./manage.py collectstatic --noinput
sleep 5
python ./manage.py migrate && python ./manage.py migrate newsroom
gunicorn -b 0.0.0.0:8000 config.wsgi app:newsroom

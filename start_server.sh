#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python3 manage.py runserver 45.91.8.248:8000
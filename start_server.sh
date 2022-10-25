#!/bin/bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 45.91.8.248:8000
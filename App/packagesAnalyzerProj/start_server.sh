#!/bin/bash

npm install npm-registry-fetch@11.0.0 --save

python3 manage.py makemigrations
python3 manage.py migrate --noinput
python3 manage.py runserver 0.0.0.0:8000
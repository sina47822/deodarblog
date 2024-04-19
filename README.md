# deodarblog
blog/django

'''bash
python -m venv env 
pip install django-admin
pip install django
'''bash

django-admin startproject projectname
cd /root/project/name

python manage.py startapp blog
python manage.py startapp core

python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

#...add all file to git

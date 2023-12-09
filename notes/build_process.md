# Build Process

1. `pipenv install django django-rest-framework docutils black isort`
1. `pipenv shell`
1. `django-admin startproject config`
1. `django-admin startapp favorites`
1. `python manage.py migrate`
1. `python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp`

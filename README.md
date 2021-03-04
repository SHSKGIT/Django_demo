# Django_demo
A Django web app deployed in docker containers.

Container cluster:
  Container 1: Django + uWSGI server
  Container 2: Nginx
  Container 3: MySQL
  Container 4: Redis
  
Container 3 & 4 are not set, but the web app can be accessed by the port Nginx exposed.

Some sensitive configurations were removed in settings.py

This is the webapp for Omni Notes written in Django, it uses mysql as the backend, however if you wish to use a different backend then you need to modify the settings.py file & put the details of the backend that you want to wish there.

Python 2.7, Django 1.7.1

Usage:

>It would be wise to make a virtualenv

1. `pip install django==1.7.1`
2. cd to the source dir
3. change the db & other settings that you want to change in `<src>/onweb/settings.py`
4. execute the manage.py file, `python manage.py runserver` This will run the server on localhost:8000

The project is released under the GNU GPL2 license

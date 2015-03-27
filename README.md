This is the webapp for Omni Notes written in Django, it uses mysql as the backend, however if you wish to use a different backend then you need to modify the settings.py file & put the details of the backend that you want to wish there.

Python 2.7, Django 1.7.1

Usage:

>It would be wise to make a virtualenv, otherwise follow the steps below

1. Install django on your machine
2. Clone the repo into some folder, `git clone https://github.com/plyrs/onweb.git`
3. `cd` to that folder
4. change the db & other settings that you want to change in `<src>/onweb/settings.py`
5. assuming you are in the onweb folder, execute the manage.py file by typing this on the terminal, `python manage.py runserver` This will run the server on localhost:8000, open localhost:8000 on your browser

The project is released under the GNU GPL2 license

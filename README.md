## Installing Python3
- Ubuntu Linux 20.04 LTS includes Python 3.8.5 by default
- Install _pip3_ (Python Package Index tool)
```
$ sudo apt install python3-pip
```

## Python virtual environment 

(ref: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment#using_django_inside_a_python_virtual_environment)

1. Install tool using pip3:
```
$ sudo pip3 install virtualenvwrapper
```

2. Setting enrironment variables

2.1. Directly, using `export` command
```
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
export PROJECT_HOME=$HOME/Devel

source /usr/local/bin/virtualenvwrapper.sh
```

2.2. Fill in `.bashrc` file

- Open file '.bashrc'
```
$ code ~/.bashrc
```
- Fill lines
```
WORKON_HOME=$HOME/.virtualenvs
VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
PROJECT_HOME=$HOME/Devel

# load virtualenvwrapper for python (after custom PATHs)
venvwrap="virtualenvwrapper.sh"
/usr/bin/which -a $venvwrap
if [ $? -eq 0 ]; then
    venvwrap=`/usr/bin/which $venvwrap`
    source $venvwrap
fi
```
- Load environment
``` 
$ source ~/.bashrc
```
###
3. Creating virtual environment
```
$ mkvirtualenv my_django_environment
```
4. Installing Django
- // Check the latest version: https://www.djangoproject.com/download/
```
$ pip3 install django~=3.1
```

###
4. Using virtual environment: commands
```
$ deactivate // Exit out of the current Python virtual environment

$ workon // List available virtual environments

$ workon my_django_environment // Activate the specified Python virtual environment

$ rmvirtualenv my_django_environment // Remove the specified environment.
```

## Create skeleton Django project
1. Create a folder contain project
```
$ mkdir django_project
$ cd django_project
```

2. Start project:
```
$ django-admin startproject mysite .
```

3. Run server
```
$ python manage.py runserver
```

4. Go to http://127.0.0.1:8000/

5. Start app
```
$ python manage.py startapp app_name
// ex: python manage.py startapp stationery
```

5.1. Registering app: `/mysite/settings.py`
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add our new application
    'app_name.apps.AppNameConfig', #This object was created for us in /app_name/apps.py
]
```
5.2. Config database: `/mysite/settings.py`
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        <!-- "OPTIONS": {
            "read_default_file": "/dj_db_config/mysql/my.cnf",
        }, -->
        "NAME": "db_name",
        "USER": "djangouser",
        "PASSWORD": "password",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
```

5.3. Using environment variable
```
import os


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USERNAME"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}
```
6. URL mapper: `/mysite/urls.py`
```
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

- `/mysite/settings.py`
```
STATIC_ROOT = BASE_DIR.joinpath("static")
```
7. Running migration
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

8. Create supper user
```
$ python manage.py createsuperuser
```

9. Manage dependencies: `requirements.txt`
```
$ pip3 freeze > requirements.txt
```

## Database setting 

(ref: https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database)
1. Install MySQL database server
```
$ sudo apt install mysql-server
```

2. Install MySQL DB connector
```
$ sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev
$ pip install mysqlclient
```

3. Create database

3.1. Create user
```
$ sudo mysql -u root
> CREATE DATABASE db_name;
> SHOW DATABASES;
> CREATE USER 'djangouser'@'%' IDENTIFIED WITH mysql_native_password BY '123456';
> GRANT ALL ON db_name.* TO 'djangouser'@'%';
> FLUSH PRIVILEGES;
```

3.2. Create file config `my.cnf`
```
[client]
database = db_name
user = djangouser
password = 123456
default-character-set = utf8
```



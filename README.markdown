#OVERNITE EVALUATOR

http://www.ktj.in/#Overnite

This is an evaluator for Overnite 2011, which is a Algorithm Competition held by IIT Kharagpur's annual Technological Fest Kshitij! As it is evident this version of software shall be used by Kshitij 2011.

This contains 3 major components:

1. Evaluator which does the actual evaluation of code files.
2. Broker which distributes load on various evaluators.
3. Web Interface, which provides a rich interface for competitors and participators.


#Installation

##Dependecies

 - Django 1.2.1 or later
 - Celery
 - djcelery
 - MySQL Server
 - Python-MySQLDB
 - RabbitMQ-Server
 - Different Compilers, in our case gcc (for C), g++ (for c++) and javac (Java Compiler)

For installing celery, djcelery and django use EasyInstall. Since, IIT KGP Proxy Polciy does not allow to use EasyInstall, we use proxychains to get through it.

##Setting up RabbitMQ

To use celery we need to create a RabbitMQ user, a virtual host and allow that user access to that virtual host:

    $ rabbitmqctl add_user myuser mypassword
    $ rabbitmqctl add_vhost myvhost
    $ rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"

##Setting up Django Project

###Database
Change database settings in seeting.py file of Web_Interface Folder. Database should be accesible from outside. To enable this feature use PHPMyAdmin. It'srecommnded to create new user having all previlages but for only one databse instead of using root.
###Broker
Change these setting accordinng to created user.

Finally setting should like like this

    SERVER = "xxx.xxx.xxx.xxx"

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'overnite',                      # Or path to database file if using sqlite3.
            'USER': 'user',                      # Not used with sqlite3.
            'PASSWORD': 'password',                  # Not used with sqlite3.
            'HOST': SERVER,                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }


    BROKER_HOST = SERVER
    BROKER_PORT = 5672
    BROKER_USER = "myuser"
    BROKER_PASSWORD = "mypassword"
    BROKER_VHOST = "myvhost"



##Running Server/Broker

Goto web_interface folder and run following command to start server

    $ python managey.py runserver

##Worker Configuration


Install Celery, django, Python-MySQLDB, djcelery and different compilers on worker computers. 
Goto worker_config folder and run following command to start worker

    $python manage.py celeryd -l info

##Test if It works

To check if everything is working, submit a code from running web_interface and see the result.


import os, djcelery
djcelery.setup_loader()
ROOT_PATH = os.path.dirname(__file__)
SERVER = "localhost"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'database_name',                  
        'USER': 'user',                     
        'PASSWORD': 'pass',                  
        'HOST': SERVER,          
        'PORT': '3306',                     
    }
}
TIME_ZONE = 'Asia/Kolkata'
INSTALLED_APPS = (
    'djcelery',
    'main',
)

BROKER_HOST = SERVER
BROKER_PORT = 5672
BROKER_USER = "user"
BROKER_PASSWORD = "pass"
BROKER_VHOST = "myvhost"


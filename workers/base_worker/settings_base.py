import os, djcelery
djcelery.setup_loader()
ROOT_PATH = os.path.dirname(__file__)

TIME_ZONE = 'Asia/Kolkata'
INSTALLED_APPS = (
    'djcelery',
    'main',
)

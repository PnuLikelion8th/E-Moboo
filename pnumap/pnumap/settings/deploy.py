from .base import *
import json

# config_secret_production = json.loads(open(CONFIG_SECRET_PRODUCTION_FILE).read())

DEBUG = False 

ALLOWED_HOSTS = ['pnumap.com','.amazonaws.com','52.78.198.136']

WSGI_APPLICATION = 'pnumap.wsgi'

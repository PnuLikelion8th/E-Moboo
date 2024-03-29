from .base import *
import json

# config_secret_production = json.loads(open(CONFIG_SECRET_PRODUCTION_FILE).read())

DEBUG = False 

ALLOWED_HOSTS = ['www.pnumap.com','pnumap.com','.amazonaws.com','52.78.198.136']

WSGI_APPLICATION = 'pnumap.wsgi'

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DB_PW = config_secret_deploy['django']['db']['password']
DB_NAME = config_secret_deploy['django']['db']['name']
DB_USER = config_secret_deploy['django']['db']['user']
DB_HOST = config_secret_deploy['django']['db']['host']

DATABASES = {
                'default': {
                      'ENGINE': 'django.db.backends.postgresql',
                      'NAME': DB_NAME,
                      'USER': DB_USER,
                      'PASSWORD': DB_PW,
                      'HOST': DB_HOST,
                      'PORT': '5432',
                }
}

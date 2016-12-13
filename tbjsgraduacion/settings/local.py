# -*- encoding: utf-8 -*-
from .base import *
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		#'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		'NAME': 'bd_tbjsgraduacion',
		'USER': 'root',
		'PASSWORD': '',
		'HOST': '127.0.0.1',
		'PORT': '3306',
	}
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)
TEMPLATE_DIRS = (
	os.path.join(BASE_DIR, 'Plantillas'),
)
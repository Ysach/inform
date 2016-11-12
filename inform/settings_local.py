import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES_Sqlite = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES_Mysql = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'info',
        'HOST': '127.0.0.1',
        'USER': 'info',
        'PASSWORD': 'info'
    }
}
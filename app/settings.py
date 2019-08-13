import os

VERSION = '0.0.1'

# Base directory of service
APP_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(APP_DIR)

HTTP_SERVER_HOST = "0.0.0.0"
HTTP_SERVER_PORT = 8000

MAX_ASYNC_TASK_CLOSE_TIME = 2

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '{asctime} | {name} | {module} | {levelname} | {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
    },
    'loggers': {
        'web_api': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console'],
        'propagate': True,
    },
}

try:
    from local_settings import *
except ImportError:
    pass

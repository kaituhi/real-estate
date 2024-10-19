from __future__ import absolute_import  

import os

from celery import Celery
from real_estate.settings import base

# Set the default Django settings module to the development settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "real_estate.settings.development")

app = Celery("real_estate")

# Configure the Celery application using the development settings, with a namespace for the settings
app.config_from_object("real_estate.settings.development", namespace="CELERY") 

# Automatically find and load any tasks defined in the installed apps of the project
app.autodiscover_tasks(lambda: base.INSTALLED_APPS)

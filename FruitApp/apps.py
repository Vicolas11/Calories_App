from django.apps import AppConfig
from django.conf import settings
from keras.models import load_model
import os


class FruitappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FruitApp'
    filename = 'model.h5'
    path = os.path.join(settings.MODEL, filename)    
    model = load_model(path)

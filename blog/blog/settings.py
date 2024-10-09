import os
from dotenv import load_dotenv
from pathlib import Path

# Rutas para archivos de medios
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Rutas para archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']


# Carga las variables del archivo .env
load_dotenv()

DJANGO_ENV = os.getenv('DJANGO_ENV', 'development') # 'development' por defecto

if DJANGO_ENV == 'production':
 from .configurations.production import *
else:
 from .configurations.local import *
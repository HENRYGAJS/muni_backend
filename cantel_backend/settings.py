"""
Django settings for cantel_backend project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n$r%i@4&+jlogqn8qggcy!zv$)o$p^9)iocm11stv$8ft!lft8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =False

ALLOWED_HOSTS = ['muni-backend.onrender.com', '127.0.0.1', 'localhost']


# settings.py

# Usar cookies seguras solo a través de HTTPS (importante si tienes habilitado HTTPS)
SESSION_COOKIE_SECURE = True

# Prevenir que las cookies de sesión sean accesibles desde JavaScript (protección contra ataques XSS)
SESSION_COOKIE_HTTPONLY = True

# Definir el tiempo de expiración de la sesión (en segundos)
# Aquí definimos 10 minutos (600 segundos)
SESSION_COOKIE_AGE = 600

# Cerrar la sesión automáticamente cuando se cierre el navegador
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Configurar una política de referer segura para evitar que se comparta información de origen sensible
SECURE_REFERRER_POLICY = 'same-origin'


# Cierra la sesión cuando el navegador se cierre
SESSION_EXPIRE_AT_BROWSER_CLOSE = True






X_FRAME_OPTIONS = 'DENY'  # Evitar que la página sea cargada en un iframe
SECURE_BROWSER_XSS_FILTER = True  # Filtro anti-XSS del navegador
SECURE_CONTENT_TYPE_NOSNIFF = True  # Evita que el navegador adivine el tipo de contenido


# Application definition

INSTALLED_APPS = [
    'storages',
    'axes',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'noticias',
    'rest_framework',
    'corsheaders',
]



# settings.py



AUTHENTICATION_BACKENDS = (
    'axes.backends.AxesStandaloneBackend',  # Cambiar al nuevo backend
    'django.contrib.auth.backends.ModelBackend',
)



JAZZMIN_SETTINGS = {
    "site_title": "Administración Cantel",
    "site_header": "Municipalidad de Cantel",
    "site_brand": "Cantel",
    "welcome_sign": "Municipalidad de Cantel Administracion 2024-2028",
    "copyright": "Municipalidad de Cantel",
    "search_model": "auth.User",  # Modelo de búsqueda en la barra superior

    # Fondo de la barra lateral
    "navigation_background_color": "bg-primary",
    "topmenu_links": [
        # Enlaces adicionales en el menú superior
        {"name": "Inicio", "url": "admin:index", "permissions": ["auth.view_user"]},
    ],
    
    # Colores personalizados para el tema
    "theme": "cosmo",  # Otros temas: cerulean, darkly, flatly, lumen, etc.
    
    # Íconos en los módulos
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },

    # Logo personalizado
    #"site_logo": "ruta/a/tu/logo.png",  # Cambia esta ruta al logo que desees
}



MIDDLEWARE = [
    
    'axes.middleware.AxesMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'cantel_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cantel_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'municipalidad_cantel',
#        'USER': 'root',
#        'PASSWORD': '12345678',
#        'HOST': 'localhost',
#        'PORT': '3306',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'municipalidad_cantel',
        'USER': 'munidb',
        'PASSWORD': 'Muni2024admin',
        'HOST': 'db-muni.cbwe0gmysorw.us-east-2.rds.amazonaws.com',
        'PORT': '3306',
    }
}




# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]





# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

#LANGUAGE_CODE = 'en-us'

#IME_ZONE = 'UTC'

#USE_I18N = True

#USE_TZ = True



LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Guatemala'  

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/




# Definir el bucket de S3 para archivos estáticos y media
#AWS_ACCESS_KEY_ID = '***REMOVED***'  # Reemplaza con tu Access Key ID de AWS
#AWS_SECRET_ACCESS_KEY = '***REMOVED***'  # Reemplaza con tu Secret Access Key de AWS
#AWS_STORAGE_BUCKET_NAME = 'municipalidad-cantel-media' # Reemplaza con el nombre de tu bucket S3
#AWS_S3_REGION_NAME = 'us-east-2' # Reemplaza con tu región, si es diferente
#AWS_S3_FILE_OVERWRITE = False
#AWS_DEFAULT_ACL = None
#AWS_S3_VERITY = True
#AWS_S3_CUSTOM_DOMAIN = 'https://municipalidad-cantel-media.s3.us-east-2.amazonaws.com'

# Configurar la ubicación de los archivos estáticos en S3
#STATIC_URL = 'https://municipalidad-cantel-media.s3.us-east-2.amazonaws.com/static/'
#MEDIA_URL = 'https://municipalidad-cantel-media.s3.us-east-2.amazonaws.com/media/'

# Usar S3 para almacenar archivos estáticos y media
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


import os
from decouple import config

# Credenciales de AWS
AWS_ACCESS_KEY_ID = '***REMOVED***'
AWS_SECRET_ACCESS_KEY = '***REMOVED***'
AWS_STORAGE_BUCKET_NAME = 'municipalidad-cantel-media'
AWS_S3_REGION_NAME = 'us-east-2'

# Configuración de AWS S3
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True
AWS_S3_CUSTOM_DOMAIN = 'municipalidad-cantel-media.s3.us-east-2.amazonaws.com'

# Configurar la ubicación de los archivos estáticos en S3
#STATIC_URL = 'municipalidad-cantel-media.s3.us-east-2.amazonaws.com/static/'
#MEDIA_URL = 'municipalidad-cantel-media.s3.us-east-2.amazonaws.com/media/'
STATIC_URL = 'https://municipalidad-cantel-media.s3.us-east-2.amazonaws.com/static/'
MEDIA_URL = 'https://municipalidad-cantel-media.s3.us-east-2.amazonaws.com/media/'
# Usar S3 para almacenar archivos estáticos y media
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Configuración del almacenamiento para archivos estáticos y media
STORAGES = {
    "default": {
        "BACKEND": 'storages.backends.s3boto3.S3Boto3Storage',
        "OPTIONS": {
            "access_key": AWS_ACCESS_KEY_ID,
            "secret_key": AWS_SECRET_ACCESS_KEY,
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            "region_name": AWS_S3_REGION_NAME,
        },
    },
    "staticfiles": {
        "BACKEND": 'storages.backends.s3boto3.S3Boto3Storage',
    },
}




#STATIC_URL = '/static/'
#MEDIA_URL = '/media/'





# Si tienes archivos estáticos locales (para desarrollo local)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Archivos estáticos (CSS, JavaScript, imágenes)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Configuración adicional de S3
AWS_QUERYSTRING_AUTH = False  # Esto desactiva las firmas en las URLs generadas, útil si tus archivos son públicos
AWS_DEFAULT_ACL = None  # Se recomienda establecer esto en 'None' para evitar problemas de permisos en S3

# Otras configuraciones de seguridad relacionadas con HTTPS (ajusta según sea necesario)




###

# Configuración de archivos medios
#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configuración de archivos estáticos
#STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ALLOW_ALL_ORIGINS = True
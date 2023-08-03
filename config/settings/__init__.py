from .environment_variables import *
from .installed_apps_configs import INSTALLED_APPS
from .middlewares_configs import MIDDLEWARE

from .auth_password_validators_configs import AUTH_PASSWORD_VALIDATORS
from .database_configs import DATABASES
from .static_files_config import STATIC_URL
from .template_configs import TEMPLATES
from .internationalization_configs import *


ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

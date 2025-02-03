from dotenv import load_dotenv
from os import getenv,path
from .base import * # noqa
from .base import BASE_DIR

local_env_file=path.join(BASE_DIR, ".envs",".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)

# SECRET_KEY = 'django-insecure-z!belh)bpx%nl69pc$)g-&o(5u6oko$5!x4=-oug6)(fi&ky8r'
SECRET_KEY  = getenv("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

DEBUG = getenv("DEBUG")

SITE_NAME =getenv('SITE_NAME')

ALLOWED_HOSTS = ["localhost","127.0.0.1","0.0.0.0"]

ADMIN_URL = getenv("ADMIN_URL")

EMAIL_BACKEND = "djcelery_emil.backends.CeleryEmailBackend"
EMAIL_HOST = getenv("EMAIL_HOST")
EMAIL_PORT = getenv("EMAIL_PORT")
DEFAULT_FROM_EMAIL = getenv("DEFAULT_FROM_EMAIL")
DOMAIN =getenv("DOMAIN")

MAX_UPLOAD_SIZE = 1 * 1024 * 1024
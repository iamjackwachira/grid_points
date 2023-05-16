from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------

DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="utew7ltTt0lOB0JJBJN2qg24WnAWkSoiEtJXviKMWy9mBydMT2lcrXHnSHlhfuHd",
)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["*"])

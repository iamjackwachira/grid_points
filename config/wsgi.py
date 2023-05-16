"""
WSGI config for grid_points project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

app_path = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
)
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(app_path, "grid_points"))

application = get_wsgi_application()

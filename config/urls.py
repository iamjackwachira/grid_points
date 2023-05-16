"""grid_points URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from . import api

public_apis = [
    path("api/v1/", include(api)),
]

schema_view = get_schema_view(
    openapi.Info(
        title="GRID POINTS DOCS",
        default_version="v1",
        description="GRID POINTS APIs",
        terms_of_service="",
        contact=openapi.Contact(email="iamjackwachira@gmail.com"),
    ),
    permission_classes=(permissions.AllowAny,),
    public=False,
    patterns=public_apis,
)

docs = [
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=None),
        name="schema-swagger-ui",
    )
]

urlpatterns = public_apis + docs + [path("admin/", admin.site.urls)]

urlpatterns += staticfiles_urlpatterns()  # type: ignore

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

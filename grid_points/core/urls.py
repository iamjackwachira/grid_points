from django.urls import include, re_path
from rest_framework import routers

from . import views

app_name = "core"

router = routers.SimpleRouter()
router.register(r"points", views.GridPointsView, "points")

urlpatterns = [
    re_path(r"^", include(router.urls)),
]

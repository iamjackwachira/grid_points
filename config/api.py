from django.urls import include, path

urlpatterns = [
    path("", include("grid_points.core.urls")),
]

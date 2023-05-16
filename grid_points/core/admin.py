from django.contrib import admin

from . import models


class GridPointAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_on",
        "received_points",
        "closest_points",
    )
    display = "GridPoint Admin"


admin.site.register(models.GridPoint, GridPointAdmin)

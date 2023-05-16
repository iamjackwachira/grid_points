from django.db import models


class GridPoint(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    modified_on = models.DateTimeField(auto_now=True, editable=False)
    received_points = models.CharField(max_length=200)
    closest_points = models.CharField(max_length=200)

    class Meta:
        ordering = ("-created_on",)
        verbose_name = "Grid Point"
        verbose_name_plural = "Grid Points"

    def __str__(self):
        return f"{self.closest_points}"

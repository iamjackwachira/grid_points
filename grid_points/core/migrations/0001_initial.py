# Generated by Django 4.2.1 on 2023-05-16 19:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GridPoint",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                ("received_points", models.CharField(max_length=200)),
                ("closest_points", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Grid Point",
                "verbose_name_plural": "Grid Points",
                "ordering": ("-created_on",),
            },
        ),
    ]

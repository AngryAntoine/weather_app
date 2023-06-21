# Generated by Django 4.2.2 on 2023-06-21 07:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("forecast", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="forecast",
            name="task_id",
            field=models.UUIDField(blank=True, default="", verbose_name="Task id the forecast was retrieved by"),
        ),
    ]

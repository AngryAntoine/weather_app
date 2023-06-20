from django.db import models


class WeatherScraperTaskStatus(models.TextChoices):
    FAILURE = "FAILURE", "Failure"
    PENDING = "PENDING", "Pending"
    STARTED = "STARTED", "Started"
    SUCCESS = "SUCCESS", "Success"

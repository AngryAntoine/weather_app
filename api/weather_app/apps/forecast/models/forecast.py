from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext as _

from weather_app.apps.common import models as core_models


class Forecast(core_models.CoreModel):
    """
    Represents a weather forecast for a day.
    """

    date = models.DateField(verbose_name=_("Denotes the measurement date"))
    temperature = models.PositiveIntegerField(
        validators=[MaxValueValidator(70)], verbose_name=_("Temperature value for the day")
    )
    description = models.TextField(
        blank=True, default=_("No extra information for this day."), verbose_name=_("Explicit description for the day")
    )
    task_id = models.UUIDField(max_length=255, blank=True, default="")

    def __str__(self):
        return f"{self.date} - {self.temperature}°C"

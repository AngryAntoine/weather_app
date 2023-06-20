from rest_framework import serializers

from weather_app.apps.forecast import models as forecast_models


class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = forecast_models.Forecast
        fields = ("date", "temperature", "description")

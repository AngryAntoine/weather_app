from rest_framework import serializers

from weather_app.apps.common import choices as common_choices
from weather_app.apps.common import serializers as common_serializers
from weather_app.apps.forecast import models as forecast_models


class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = forecast_models.Forecast
        fields = ("date", "temperature", "description", "task_id", "updated")


class RefreshForecastSerializer(common_serializers.CoreSerializer):
    period = serializers.IntegerField(min_value=1, max_value=10, required=False)


class ForecastCheckStatusSerializer(common_serializers.CoreSerializer):
    task_id = serializers.UUIDField(required=True)


class ForecastCheckStatusResponseSerializer(common_serializers.CoreSerializer):
    status = serializers.ChoiceField(choices=common_choices.WeatherScraperTaskStatus.choices)

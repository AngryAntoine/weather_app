from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from weather_app.apps.forecast import selectors as forecast_selectors
from weather_app.apps.forecast.api.v1 import serializers as forecast_serializers


@extend_schema_view(
    get=extend_schema(summary="Forecast list", tags=["Forecast"]),
)
class ForecastListAPIView(ListAPIView):
    serializer_class = forecast_serializers.ForecastSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return forecast_selectors.get_all_forecasts()


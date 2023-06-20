from django.urls import path

from weather_app.apps.forecast.api.v1 import views as forecast_views

urlpatterns = [
    path("", forecast_views.ForecastListAPIView.as_view(), name="forecast-list"),
]

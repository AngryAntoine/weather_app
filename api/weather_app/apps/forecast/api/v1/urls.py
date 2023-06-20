from django.urls import path

from weather_app.apps.forecast.api.v1 import views as forecast_views


urlpatterns = [
    path("", forecast_views.ForecastListAPIView.as_view(), name="forecast-list"),
    path("refresh/", forecast_views.RefreshForecastAPIView.as_view(), name="forecast-refresh"),
    path(
        "refresh/check-status/",
        forecast_views.CheckForecastRefreshStatusAPIView.as_view(),
        name="check-refresh-status",
    ),
]

from django.conf import settings

from weather_app.apps.forecast import services as forecast_services
from weather_app.celery import celery_app as app


@app.task
def get_weather_forecast(period: int):
    """
    A task to perform the forecast retrieving from the external service
    """
    forecast_parser_service = forecast_services.BSForecastParserService(url=settings.WEATHER_URL["meta_weather"])
    forecast_service = forecast_services.ForecastService()
    forecasts = forecast_parser_service.get_forecast(period=period)
    forecast_service.update_or_create(task_id=get_weather_forecast.request.id, forecasts=forecasts)

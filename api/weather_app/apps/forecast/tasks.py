from weather_app.celery import celery_app as app
from weather_app.apps.forecast import services as forecast_services


@app.task
def get_weather_forecast():
    """
    A task to perform the forecast retrieving from the external service
    """
    forecast_service = forecast_services.ForecastService()

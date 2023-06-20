from weather_app.apps.forecast.models import Forecast


def get_all_forecasts():
    return Forecast.objects.active()

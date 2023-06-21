from celery.schedules import crontab

from ..django import TIME_ZONE as DJANGO_TIME_ZONE
from ..environment import env


CELERY_TASK_ALWAYS_EAGER = env.bool("WEATHER_APP_CELERY_TASK_ALWAYS_EAGER", default=False)
CELERY_BROKER_URL = env.str("WEATHER_APP_CELERY_BROKER", default="redis://redis:6379/1")
CELERY_TASK_TRACK_STARTED = True
CELERY_IGNORE_RESULT = False
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = DJANGO_TIME_ZONE


CELERY_BEAT_SCHEDULE = {
    "retrieve_forecast": {
        "task": "weather_app.apps.forecast.tasks.get_weather_forecast",
        "schedule": crontab(hour="9"),
        "kwargs": {"period": 6},
    },
}

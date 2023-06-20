from ..django import TIME_ZONE as DJANGO_TIME_ZONE
from ..environment import env
from celery.schedules import crontab


CELERY_TASK_ALWAYS_EAGER = env.bool("WEATHER_APP_CELERY_TASK_ALWAYS_EAGER", default=False)
CELERY_BROKER_URL = env.str("WEATHER_APP_CELERY_BROKER", default="redis://redis:6379/1")

CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = DJANGO_TIME_ZONE


CELERY_BEAT_SCHEDULE = {
    "make_drivers_available": {
        "task": "ironcans.apps.accounts.tasks.make_drivers_available",
        "schedule": crontab(minute="*/1"),
    },
    "calculate_routes_for_today": {
        "task": "ironcans.apps.dispatching.tasks.calculate_routes_for_active_companies_for_today",
        "schedule": crontab(minute=10, hour=0),
    },
}

from django.contrib import admin

from weather_app.apps.forecast.models import Forecast


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ("date", "temperature", "description", "updated")
    search_fields = ("date",)
    ordering = ("date",)

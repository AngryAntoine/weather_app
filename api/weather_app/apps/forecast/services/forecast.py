from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List
from uuid import UUID

import requests

from bs4 import BeautifulSoup as BS
from bs4 import Tag

from weather_app.apps.forecast import models as forecast_models


@dataclass(kw_only=True, frozen=True)
class ForecastForDay:
    """
    The forecast for a given day
    """

    date: datetime
    temperature: int
    description: str


class BaseForecastParserService(ABC):
    @abstractmethod
    def get_forecast(self, period: int) -> None:
        """
        Retrieves the forecast for the next N days
        """
        pass


class BSForecastParserService(BaseForecastParserService):
    """
    Beautiful Soup forecast parser service
    """

    def __init__(self, url: str, city: str = "Kyiv", region: str = "Kyivskiy", county: str = "Kyivska") -> None:
        self.url = url
        self.city = city
        self.region = region
        self.county = county

    def _get_data(self, date: datetime.date) -> Tag | None:
        """
        Retrieves the full forecast data for a given date
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        date_to_str = date.strftime("%Y-%m-%d")
        url = f"{self.url}/{self.county}/{self.region}/{self.city}/{date_to_str}/ajax/"
        try:
            response = requests.get(url, headers=headers)
            return BS(response.content, "html.parser").find("div", class_="city__main-inner")
        except requests.HTTPError:
            pass

    @staticmethod
    def _get_temperature(*, day: Tag) -> int:
        """
        Retrieves the temperature for a given day, removing the unnecessary symbols
        """
        return int(day.find("div", class_="city__main-temp").text.replace("°", "").replace("+", ""))

    @staticmethod
    def _get_description(*, day: Tag) -> str:
        """
        Retrieves the description for a given day, removing the unnecessary symbols
        """
        lines = day.find_all("span", class_="city__main-image-descr")
        res_str = []
        for line in lines:
            res_str.append(line.text.replace(".", "").replace("\n", ""))
        return ", ".join(res_str)

    def get_forecast(self, period: int = 6) -> List[ForecastForDay]:
        """
        Get forecast for the given period, default is today's date plus 5 next days
        """
        forecasts = []
        for item in range(0, period):
            date = datetime.now() + timedelta(days=item)
            soup_data = self._get_data(date=date)
            if soup_data is not None:
                forecast_data = {
                    "date": date,
                    "temperature": self._get_temperature(day=soup_data),
                    "description": self._get_description(day=soup_data),
                }
                forecasts.append(ForecastForDay(**forecast_data))
        return forecasts


class ForecastService:
    """
    Forecast service to deal with Forecast models manipulations
    """
    @staticmethod
    def update_or_create(*, task_id: UUID, forecasts: List[ForecastForDay]) -> None:
        """
        Creates or updates the forecast
        """
        for forecast in forecasts:
            forecast_models.Forecast.objects.update_or_create(
                date=forecast.date,
                defaults={
                    "task_id": task_id,
                    "temperature": forecast.temperature,
                    "description": forecast.description,
                },
            )

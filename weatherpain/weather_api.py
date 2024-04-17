import requests
from datetime import datetime
import sys
from weather_au import api

class WeatherService:
    def __init__(self, location_code):
        self.location_code = location_code
        self.weather_api = api.WeatherApi(search=self.location_code, debug=0)

    def get_location(self):
        location = self.weather_api.location()
        if location is None:
            sys.exit(f'Search failed for location {self.location_code}')
        return location

    def get_warnings(self):
        warnings = self.weather_api.warnings()
        if warnings is None:
            return []
        return warnings

    def get_observations(self):
        observations = self.weather_api.observations()
        if observations is None:
            return {}
        return observations

    def get_forecast_rain(self):
        forecast_rain = self.weather_api.forecast_rain()
        if forecast_rain is None:
            return {}
        return forecast_rain

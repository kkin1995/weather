import requests
from decouple import config

secret_key = config('api_key')


url_for_location_key = "http://dataservice.accuweather.com/locations/v1/cities/search"
language = "en-us"

params = {
    "apikey": secret_key,
    "q": "Bengaluru",
    "language": language,
}

request_for_loc_key = requests.get(url = url_for_location_key, params = params)

bengaluruKey = request_for_loc_key.json()[0]["Key"]

url_for_1hour_forecast = "http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/" + bengaluruKey

params_forecast = {
    "apikey": secret_key,
    "language": language,
    "metric": True
}

request_for_forecast = requests.get(url = url_for_1hour_forecast, params = params_forecast)

forecast_data = request_for_forecast.json()[0]

print("Temperature for Bangalore is {} {}".format(forecast_data["Temperature"]["Value"], forecast_data["Temperature"]["Unit"]))
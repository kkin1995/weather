import requests
import time
from decouple import config

def get_forecast(secret_key, location):
    language = "en-us"
    url_for_location_key = "http://dataservice.accuweather.com/locations/v1/cities/search"
    params = {
        "apikey": secret_key,
        "q": location,
        "language": language,
    }
    request_for_loc_key = requests.get(url = url_for_location_key, params = params)
    print(request_for_loc_key)
    locationKey = request_for_loc_key.json()[0]["Key"]
    url_for_1hour_forecast = "http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/" + locationKey
    params_forecast = {
        "apikey": secret_key,
        "language": language,
        "metric": True
    }
    request_for_forecast = requests.get(url = url_for_1hour_forecast, params = params_forecast)
    forecast_data = request_for_forecast.json()[0]

    return forecast_data


if __name__ == '__main__':
    secret_key = config('api_key')
    location = "Mumbai"
    forecast_data = get_forecast(secret_key, location)
    date_forecast = forecast_data["DateTime"].split("T")[0]
    time_forecast = forecast_data["DateTime"].split("T")[1]
    temperature = forecast_data["Temperature"]["Value"]
    print("The temperature for {} is {} on {}".format(location, temperature, date_forecast + time_forecast))
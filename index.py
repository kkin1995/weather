from flask import Flask
from weather import get_forecast
from decouple import config

secret_key = config("api_key")

location = "Bengaluru"
#forecast_data = get_forecast(secret_key, location)
#date_forecast = forecast_data["DateTime"].split("T")[0]
#time_forecast = forecast_data["DateTime"].split("T")[1]
#temperature = forecast_data["Temperature"]["Value"]

app = Flask(__name__)

@app.route('/')
def index():
    return location
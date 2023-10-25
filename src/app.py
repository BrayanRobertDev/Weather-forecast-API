from dotenv import load_dotenv
import os
from weather_forecast import CityData
from flask import Flask, Response
import json

load_dotenv()
key = os.getenv("KEY")

app = Flask(__name__)


@app.route('/city_temperature/<city_name>')
def getTemperatureCity(city_name):
    city_data = CityData(city_name, key)
    temperature = city_data.getTemperature()
    climate = city_data.getClimate()
    humidity = city_data.getHumidity()
    pressure = city_data.getPressure()
    wind = city_data.getWind()
    data = {
        "city" : city_name,
        "temperature" : temperature,
        "climate" : climate,
        "humidity" : humidity,
        "pressure" : pressure,
        "wind" : wind*3.6
    }
    response = Response(json.dumps(data, ensure_ascii=False).encode('utf-8'))
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
from dotenv import load_dotenv
import os
from weather_forecast import CityData
from flask import Flask, Response, json
from flask_cors import CORS

load_dotenv()
key = os.getenv("KEY")

app = Flask(__name__)
CORS(app)

@app.route('/city_temperature/<city_name>')
def getTemperatureCity(city_name):
    try:
        city_data = CityData(city_name, key)
        temperature = city_data.getTemperature()
        climate = city_data.getClimate()
        humidity = city_data.getHumidity()
        pressure = city_data.getPressure()
        wind = city_data.getWind()
        data = {
            "city": city_name,
            "temperature": temperature,
            "climate": climate,
            "humidity": humidity,
            "pressure": pressure,
            "wind": wind * 3.6
        }
        response = Response(json.dumps(data, ensure_ascii=False).encode('utf-8'))
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    except Exception as e:
        error_message = {"error": str(e)}
        response = Response(json.dumps(error_message).encode('utf-8'), status=500)
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

@app.errorhandler(404)
def not_found_error(error):
    error_message = {"error": "Página não encontrada"}
    response = Response(json.dumps(error_message).encode('utf-8'), status=404)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

@app.errorhandler(500)
def internal_server_error(error):
    error_message = {"error": "Erro interno do servidor"}
    response = Response(json.dumps(error_message).encode('utf-8'), status=500)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

if __name__ == '__main__':
    app.run(debug=True)

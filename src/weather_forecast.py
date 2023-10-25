import requests
from dataclasses import dataclass
@dataclass
class CityData:
    _city: str
    _key: str

    def __post_init__(self):
        self._url = f"http://api.openweathermap.org/data/2.5/weather?q={self._city}&appid={self._key}&units=metric"
        self._response = requests.get(self._url)
        self._data = self._response.json()

    def getTemperature(self):
        return self._data['main']['temp']
    
    def getClimate(self):
        return self._data['weather'][0]['description']
    
    def getHumidity(self):
        return self._data['main']['humidity']
    
    def getPressure(self):
        return self._data['main']['pressure']
    
    def getWind(self):
        return self._data['wind']['speed']


    




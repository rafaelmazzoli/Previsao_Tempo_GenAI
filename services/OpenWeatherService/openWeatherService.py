import requests
from decouple import config

class OpenWeatherService:
    UNIDADE_METRICA = "metric"
    LINGUAGEM = "pt_br"

    def __init__(self):
        self.API_KEY = config('API_KEY_OPEN_WEATHER_SERVICE')

    def buscarLatitudeLongitude(self, nomeCidade, codigoEstado = "", codigoPais = ""):
        try:
            response = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=" + nomeCidade + "," + codigoEstado + "," + codigoPais + "&limit=1&appid=" + self.API_KEY)

            data = response.json()

            if response.status_code != 200:
                raise requests.exceptions.RequestException(response.status_code, data)

            latitude = data[0]['lat']
            longitude = data[0]['lon']
            
            return { 'latitude': latitude, 'longitude': longitude }

        except requests.exceptions.RequestException as e:
            print(f'Erro na solicitação: {e}')

    def buscarPrevisaoDoTempoHoje(self, latitude, longitude):
        try:
            response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + str(latitude) + "&lon=" + str(longitude) + "&units=" + self.UNIDADE_METRICA + "&lang=" + self.LINGUAGEM + "&appid=" + self.API_KEY)

            data = response.json()

            if response.status_code != 200:
                raise requests.exceptions.RequestException(response.status_code, data)

            return data

        except requests.exceptions.RequestException as e:
            print(f'Erro na solicitação: {e}')

    def buscarPrevisaoDoTempo5Dias(self, latitude, longitude):
        try:
            response = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=" + str(latitude) + "&lon=" + str(longitude) + "&units=" + self.UNIDADE_METRICA + "&lang=" + self.LINGUAGEM + "&appid=" + self.API_KEY)

            data = response.json()

            if response.status_code != 200:
                raise requests.exceptions.RequestException(response.status_code, data)

            return data

        except requests.exceptions.RequestException as e:
            print(f'Erro na solicitação: {e}')
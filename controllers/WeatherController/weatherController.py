import pandas as pd
from datetime import datetime

class WeatherController:
    def __init__(self, previsaoDoTempoHoje, previsaoDoTempo5Dias):
        self.previsaoDoTempoHoje = previsaoDoTempoHoje
        self.previsaoDoTempo5Dias = previsaoDoTempo5Dias

    def gerarDataFrameTemperaturasOpenWeatherPor3Horas(self):
        index = []
        conteudo = {
            "Temperatura": [],
            "Humidade do Ar": [],
            "Clima": []
        }

        for previsaoDoTempo in self.previsaoDoTempo5Dias['list']:
            dataFormatada = datetime.utcfromtimestamp(previsaoDoTempo['dt'])

            index.append(dataFormatada.strftime('%d/%m/%Y %H:%M'))
            conteudo['Temperatura'].append(round(previsaoDoTempo['main']['temp']))
            conteudo['Humidade do Ar'].append(previsaoDoTempo['main']['humidity'])
            conteudo['Clima'].append(previsaoDoTempo['weather'][0]['description'])
        
        return pd.DataFrame(conteudo, index)

    def gerarDataFrameTemperaturasOpenWeatherPorDia(self):
        index = []
        conteudo = {
            "Temperatura Máxima": [],
            "Temperatura Mínima": [],
            "Humidade do Ar": [],
            "Clima": []
        }
        
        # Adiciona o Dia de Hoje
        index.append(datetime.now().strftime('%d/%m/%Y'))
        conteudo['Temperatura Máxima'].append(round(self.previsaoDoTempoHoje['main']['temp_max']))
        conteudo['Temperatura Mínima'].append(round(self.previsaoDoTempoHoje['main']['temp_min']))
        conteudo['Humidade do Ar'].append(self.previsaoDoTempoHoje['main']['humidity'])
        conteudo['Clima'].append(self.previsaoDoTempoHoje['weather'][0]['description'])

        # Adiciona os próximos dias
        dia = None
        temperaturasMaximas = []
        temperaturasMinimas = []
        humidades = []
        clima = None

        for previsaoDoTempo in self.previsaoDoTempo5Dias['list']:
            dataFormatada = datetime.utcfromtimestamp(previsaoDoTempo['dt'])

            if(dataFormatada.hour == 0):
                dia = dataFormatada
                temperaturasMaximas = []
                temperaturasMinimas = []
                humidades = []
                clima = None

            # Pular os dias que não possuem previsão completa desde às 00h00
            if(dia != dataFormatada.replace(hour=0)):
                continue

            if(dataFormatada.hour == 12):
                clima = previsaoDoTempo['weather'][0]['description']
            
            humidades.append(previsaoDoTempo['main']['humidity'])
            temperaturasMaximas.append(round(previsaoDoTempo['main']['temp_max']))
            temperaturasMinimas.append(round(previsaoDoTempo['main']['temp_min']))

            if(dataFormatada.hour == 21):
                index.append(dia.strftime('%d/%m/%Y'))
                conteudo['Temperatura Máxima'].append(max(temperaturasMaximas))
                conteudo['Temperatura Mínima'].append(min(temperaturasMinimas))
                conteudo['Humidade do Ar'].append(round(sum(humidades) / len(humidades)))
                conteudo['Clima'].append(clima)

        return pd.DataFrame(conteudo, index)

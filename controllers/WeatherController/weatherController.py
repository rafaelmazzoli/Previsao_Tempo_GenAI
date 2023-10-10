import pandas as pd
from datetime import datetime

class WeatherController:
    def __init__(self, previsaoDoTempoHoje, previsaoDoTempo5Dias):
        self.previsaoDoTempoHoje = previsaoDoTempoHoje
        self.previsaoDoTempo5Dias = previsaoDoTempo5Dias

    def gerarDataFrameTemperaturasOpenWeatherPor3Horas(self):
        conteudo = {
            "Data": [],
            "Temperatura": [],
            "Umidade do Ar": [],
            "Clima": []
        }

        for previsaoDoTempo in self.previsaoDoTempo5Dias['list']:
            dataFormatada = datetime.utcfromtimestamp(previsaoDoTempo['dt'])

            conteudo['Data'].append(dataFormatada.strftime('%d/%m/%Y %H:%M'))
            conteudo['Temperatura'].append(round(previsaoDoTempo['main']['temp']))
            conteudo['Umidade do Ar'].append(previsaoDoTempo['main']['humidity'])
            conteudo['Clima'].append(previsaoDoTempo['weather'][0]['description'])
        
        df = pd.DataFrame(conteudo).set_index("Data")
        return df

    def gerarDataFrameTemperaturasOpenWeatherPorDia(self):
        conteudo = {
            "Data": [],
            "Temperatura Máxima": [],
            "Temperatura Mínima": [],
            "Umidade do Ar": [],
            "Clima": []
        }
        
        # Adiciona o Dia de Hoje
        conteudo['Data'].append(datetime.now().strftime('%d/%m/%Y'))
        conteudo['Temperatura Máxima'].append(round(self.previsaoDoTempoHoje['main']['temp_max']))
        conteudo['Temperatura Mínima'].append(round(self.previsaoDoTempoHoje['main']['temp_min']))
        conteudo['Umidade do Ar'].append(self.previsaoDoTempoHoje['main']['humidity'])
        conteudo['Clima'].append(self.previsaoDoTempoHoje['weather'][0]['description'])

        # Adiciona os próximos dias
        dia = None
        temperaturasMaximas = []
        temperaturasMinimas = []
        umidades = []
        clima = None

        for previsaoDoTempo in self.previsaoDoTempo5Dias['list']:
            dataFormatada = datetime.utcfromtimestamp(previsaoDoTempo['dt'])

            if(dataFormatada.hour == 0):
                dia = dataFormatada
                temperaturasMaximas = []
                temperaturasMinimas = []
                umidades = []
                clima = None

            # Pular os dias que não possuem previsão completa desde às 00h00
            if(dia != dataFormatada.replace(hour=0)):
                continue

            if(dataFormatada.hour == 12):
                clima = previsaoDoTempo['weather'][0]['description']
            
            umidades.append(previsaoDoTempo['main']['humidity'])
            temperaturasMaximas.append(round(previsaoDoTempo['main']['temp_max']))
            temperaturasMinimas.append(round(previsaoDoTempo['main']['temp_min']))

            if(dataFormatada.hour == 21):
                conteudo['Data'].append(dia.strftime('%d/%m/%Y'))
                conteudo['Temperatura Máxima'].append(max(temperaturasMaximas))
                conteudo['Temperatura Mínima'].append(min(temperaturasMinimas))
                conteudo['Umidade do Ar'].append(round(sum(umidades) / len(umidades)))
                conteudo['Clima'].append(clima)

        df = pd.DataFrame(conteudo).set_index("Data")
        return df

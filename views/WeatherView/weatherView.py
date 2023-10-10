import pandas as pd
import matplotlib.pyplot as plt

class WeatherView:
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame

    def gerarGraficoDeBarras(self):
        fig, ax = plt.subplots()
        ax.set_ylabel('Temperatura em ºC e humidade em %')
        ax.set_title('Temperatura e humidade nos próximos dias')
        ax.xaxis.set_visible(False)

        self.dataFrame.plot(table=True, kind="bar", ax=ax)

        plt.tight_layout()
        
        plt.show()

    def gerarGraficoDeLinhas(self):
        fig, ax = plt.subplots()
        ax.set_xlabel('Dia e Hora')
        ax.set_ylabel('Temperatura em ºC e humidade em %')
        ax.set_title('Temperatura e humidade nos próximos dias')

        self.dataFrame.plot(ax=ax)
        
        for tick in ax.get_xticklabels():
            tick.set_rotation(90)

        plt.tight_layout()
        
        plt.show()
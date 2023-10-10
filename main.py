from services.OpenWeatherService.openWeatherService import OpenWeatherService
from controllers.WeatherController.weatherController import WeatherController
from views.WeatherView.weatherView import WeatherView
from views.TerminalView.terminalView import TerminalView
from models.appModel import AppModel

def main():
    appConfigs = AppModel()
    openWeatherAPI = OpenWeatherService()

    terminal = TerminalView(appConfigs)

    while True:
        continua = terminal.menuPrincipal()
        if not continua:
            return

        resultadoLatLon = openWeatherAPI.buscarLatitudeLongitude(appConfigs.cidadePesquisada, appConfigs.estadoPesquisado, appConfigs.paisPesquisado)
        resultadoPrevisaoTempoHoje = openWeatherAPI.buscarPrevisaoDoTempoHoje(resultadoLatLon['latitude'], resultadoLatLon['longitude'])
        resultadoPrevisaoTempo5Dias = openWeatherAPI.buscarPrevisaoDoTempo5Dias(resultadoLatLon['latitude'], resultadoLatLon['longitude'])

        weatherControl = WeatherController(resultadoPrevisaoTempoHoje, resultadoPrevisaoTempo5Dias)
        
        if appConfigs.granularidadeDoResultado == "Por dia":
            executarFluxoPorDia(appConfigs, weatherControl)
        else:
            executarFluxoPor3Horas(appConfigs, weatherControl)
        
        input("\nPressione ENTER para continuar...")
        appConfigs.resetarVariaveis()

def executarFluxoPorDia(appConfigs, weatherControl):
    resultadoDataFrame = weatherControl.gerarDataFrameTemperaturasOpenWeatherPorDia()
    print("Previsão do Tempo para " + appConfigs.cidadePesquisada + ":\n\n")
    
    if appConfigs.exibirTabelaResultado:
        print(resultadoDataFrame)

    if appConfigs.exibirGraficoResultado:
        weatherPlots = WeatherView(resultadoDataFrame)
        weatherPlots.gerarGraficoDeBarras()

def executarFluxoPor3Horas(appConfigs, weatherControl): 
    resultadoDataFrame = weatherControl.gerarDataFrameTemperaturasOpenWeatherPor3Horas()
    print("Previsão do Tempo para " + appConfigs.cidadePesquisada + ":\n\n")
    
    if appConfigs.exibirTabelaResultado:
        print(resultadoDataFrame)

    if appConfigs.exibirGraficoResultado:
        weatherPlots = WeatherView(resultadoDataFrame)
        weatherPlots.gerarGraficoDeLinhas()


if __name__ == "__main__":
    main()
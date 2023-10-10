class AppModel:
    OPCOES_GRANULARIDADE = ["Por dia", "A cada 3 horas"]

    def __init__(self):
        self.resetarVariaveis()
        self.resetarConfiguracoes()

    def resetarVariaveis(self):
        self.cidadePesquisada = None
        self.estadoPesquisado = None
        self.paisPesquisado = None

    def resetarConfiguracoes(self):
        self.exibirGraficoResultado = True
        self.exibirTabelaResultado = True
        self.exibirAlertasDeRisco = True
        self.granularidadeDoResultado = self.OPCOES_GRANULARIDADE[0]

    def alternarVisualizacaoDoGraficoResultado(self):
        self.exibirGraficoResultado = not self.exibirGraficoResultado

    def alternarVisualizacaoDosAlertasDeRisco(self):
        self.exibirAlertasDeRisco = not self.exibirAlertasDeRisco

    def alternarVisualizacaoDaTabelaResultado(self):
        self.exibirTabelaResultado = not self.exibirTabelaResultado

    def alternarGranularidadeDoResultado(self):
        self.granularidadeDoResultado = self._proximaOpcaoDoCarrossel(self.granularidadeDoResultado, self.OPCOES_GRANULARIDADE)

    def _proximaOpcaoDoCarrossel(self, opcaoAtual, listaDeOpcoes):
        index = listaDeOpcoes.index(opcaoAtual)
        next_index = (index + 1) % len(listaDeOpcoes)
        return listaDeOpcoes[next_index]

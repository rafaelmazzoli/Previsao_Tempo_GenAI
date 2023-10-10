import os

class TerminalView:
    def __init__(self, appModel):
        self.appConfigs = appModel
        self._boasVindas()


    def _boasVindas(self):
        self._limparTela()
        print("Bem-vindo ao App de Previsão do Tempo")
        input("Pressione ENTER para continuar...")

    def _solicitarInformacoesPrevisaoDoTempo(self):
        while not self.appConfigs.cidadePesquisada:
            self._limparTela()
            self.appConfigs.cidadePesquisada = input("Nome da Cidade*: ")
        
        self.appConfigs.estadoPesquisado = input("Sigla do Estado: ")
        self.appConfigs.paisPesquisado = input("Sigla do País: ")
        self._limparTela()


    def menuPrincipal(self):
        menu = {
            '1': self._solicitarInformacoesPrevisaoDoTempo,
            '2': self._menuConfiguracoes,
            '0': None
        }
        while True:
            self._limparTela()
            print("Menu Principal:")
            print("1. Consultar Previsão do Tempo")
            print("2. Configurações")
            print("\n0. Sair")
            escolha = input("Escolha uma opção: ")
            continua = self._validarEscolha(menu, escolha)
            if not continua:
                return continua
            if escolha == "1":
                return continua

    def _menuConfiguracoes(self):
        menu = {
            '1': self._menuVisualizacao,
            '2': self._menuGranularidade,
            '9': self.appConfigs.resetarConfiguracoes,
            '0': None
        }
        while True:
            self._limparTela()
            print("Menu Configurações:")
            print("1. Visualização do Resultado")
            print("2. Granularidade do Resultado")
            print("9. Resetar Configurações Padrões")
            print("\n0. Voltar")
            escolha = input("Escolha uma opção: ")
            continua = self._validarEscolha(menu, escolha)
            if not continua:
                break

    def _menuVisualizacao(self):
        menu = {
            '1': self.appConfigs.alternarVisualizacaoDoGraficoResultado,
            '2': self.appConfigs.alternarVisualizacaoDaTabelaResultado,
            '0': None
        }
        while True:
            self._limparTela()
            print("Menu Visualização do Resultado:")
            print("1. Gráfico: " + ("Ativo" if self.appConfigs.exibirGraficoResultado else "Inativo"))
            print("2. Tabela: " + ("Ativa" if self.appConfigs.exibirTabelaResultado else "Inativa"))
            print("\n0. Voltar")
            escolha = input("Escolha uma opção: ")
            continua = self._validarEscolha(menu, escolha)
            if not continua:
                break

    def _menuGranularidade(self):
        menu = {
            '1': self.appConfigs.alternarGranularidadeDoResultado,
            '0': None
        }
        while True:
            self._limparTela()
            print("Menu Visualização do Resultado:")
            print("1. Granularidade: " + self.appConfigs.granularidadeDoResultado)
            print("\n0. Voltar")
            escolha = input("Escolha uma opção: ")
            continua = self._validarEscolha(menu, escolha)
            if not continua:
                break

    def _validarEscolha(self, menu, escolha):
        continua = True
        
        if escolha not in menu:
            print("Opção inválida. Tente novamente.")
            input("Pressione ENTER para continuar...")
            return continua
        if escolha == "0":
            return not continua
        
        menu[escolha]()
        return continua

    def _limparTela(self):
        sistema_operacional = os.name
        if sistema_operacional == 'posix':
            os.system('clear')  # Comando para limpar o terminal no Linux/macOS
        elif sistema_operacional == 'nt':
            os.system('cls')   # Comando para limpar o terminal no Windows
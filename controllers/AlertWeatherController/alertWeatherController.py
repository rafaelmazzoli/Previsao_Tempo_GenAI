class AlertWeatherController:
    def encontrarTemperaturasDeRisco(self, dataFrame):
        nomeVariavelTemperaturaMaxima = self._validarColunaTemperaturaMaxima(dataFrame)
        nomeVariavelTemperaturaMinima = self._validarColunaTemperaturaMinima(dataFrame)
        nomeVariavelUmidade = "Umidade do Ar"

        alertas = []

        for index, row in dataFrame.iterrows():
            Data = row.name
            temperaturaMaxima = row[nomeVariavelTemperaturaMaxima]
            temperaturaMinima = row[nomeVariavelTemperaturaMinima]
            umidade = row[nomeVariavelUmidade]

            if temperaturaMaxima >= 37:
                alertas.append({
                    "Título": "Calor Extremo (" + str(temperaturaMaxima) + "ºC) em " + Data,
                    "Mensagem": "Mantenha-se hidratado bebendo água regularmente, evite a exposição direta ao sol durante as horas mais quentes do dia, use roupas leves e soltas, e procure sombra ou locais com ar-condicionado quando possível."
                })
            elif temperaturaMinima <= 15:
                alertas.append({
                    "Título": "Frio Extremo (" + str(temperaturaMinima) + "ºC) em " + Data,
                    "Mensagem": "Vista-se adequadamente com roupas quentes e camadas, proteja as extremidades (mãos, pés, nariz e orelhas), evite a exposição prolongada ao frio e procure abrigo."
                })
            
            if umidade >= 80:
                alertas.append({
                    "Título": "Umidade Alta (" + str(umidade) + "%) em " + Data,
                    "Mensagem": "Use ventiladores, ar-condicionado ou desumidificadores para reduzir a umidade interna. Mantenha-se hidratado e evite atividades físicas extenuantes em condições de alta umidade."
                })
            elif umidade <= 20:
                alertas.append({
                    "Título": "Umidade Baixa (" + str(umidade) + "%) em " + Data,
                    "Mensagem": "Use um umidificador para aumentar a umidade interna, beba bastante água, e use hidratantes para a pele."
                })
            
        return alertas

    def _validarColunaTemperaturaMaxima(self, dataFrame):
        nomesAceitos = [
            "Temperatura",
            "Temperatura Máxima"
        ]
        nomeVariavelTemperatura = None

        for nomeAceito in nomesAceitos:
            if nomeAceito in dataFrame.columns.tolist():
                nomeVariavelTemperatura = nomeAceito
        
        if not nomeVariavelTemperatura:
            raise Exception("Dataframe não possui uma sas colunas necessárias: " + nomesAceitos.join(", "))
        
        return nomeVariavelTemperatura

    def _validarColunaTemperaturaMinima(self, dataFrame):
        nomesAceitos = [
            "Temperatura",
            "Temperatura Mínima"
        ]
        nomeVariavelTemperatura = None

        for nomeAceito in nomesAceitos:
            if nomeAceito in dataFrame.columns.tolist():
                nomeVariavelTemperatura = nomeAceito
        
        if not nomeVariavelTemperatura:
            raise Exception("Dataframe não possui uma sas colunas necessárias: " + nomesAceitos.join(", "))
        
        return nomeVariavelTemperatura
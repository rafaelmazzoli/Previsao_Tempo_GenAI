import ctypes

class PopUpView:
    MB_OK = 0
    MB_OKCANCEL = 1
    MB_YESNOCANCEL = 3
    MB_YESNO = 4

    IDOK = 1
    IDCANCEL = 2
    IDABORT = 3
    IDYES = 6
    IDNO = 7

    def exibirListaDeMessageBoxOkCancel(self, lista):
        for item in lista:
            result = self.exibirMessageBox(item["Título"], item["Mensagem"], self.MB_OKCANCEL)
            if not result or result == self.IDCANCEL:
                break

    def exibirMessageBox(self, titulo, mensagem, estilo):
        return ctypes.windll.user32.MessageBoxW(0, mensagem, titulo, estilo)
from noDuplo import NoDuplo

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserirNoInicio(self,valor):
        novoNo = NoDuplo(valor)
        if self.inicio is None:
            self.inicio = novoNo
            self.fim = novoNo
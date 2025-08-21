from noDuplo import NoDuplo

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
    # Funcao que insere no inicio da lista
    def inserirNoInicio(self,valor):
        novoNo = NoDuplo(valor)
        if self.inicio is None:
            self.inicio = novoNo
            self.fim = novoNo
        else:
            novoNo.proximo = self.inicio
            self.inicio.anterior =  novoNo
            self.inicio = novoNo

    # Funcao que insere no fim da lista
    def inserirNoFim(self,valor):
        novoNo = NoDuplo(valor)
        if self.inicio is None:
            self.inicio = novoNo
            self.fim = novoNo
        else:
            self.fim.proximo = novoNo
            novoNo.anterior = self.fim
            self.fim = novoNo
    # Funcao que exibe a lista do primeiro ao ultimo
    def exibirLista(self):
        if self.inicio is None:
            print("Lista Vazia!")
        else:
            aux = self.inicio
            while aux is not None:
                print(aux.valor)
                aux = aux.proximo


# ==================================================

lde1 = ListaDuplamenteEncadeada()
lde1.inserirNoFim(1)
lde1.inserirNoFim(2)
lde1.inserirNoFim(3)
lde1.inserirNoInicio(0)
lde1.inserirNoInicio(-1)

lde1.exibirLista()
            
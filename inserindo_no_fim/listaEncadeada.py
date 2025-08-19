from no import No

class listaEncadeada:
    def __init__(self):
        self.primeiro = None # Inicio da lista, "None" pois a lista sempre inicia vazia

    def inserirNoFim(self,dado):
        novoNo = No(dado)
        if self.primeiro == None:
            self.primeiro = novoNo
        else:
            noAtual = self.primeiro
            while noAtual.proximo is not None:
                noAtual = noAtual.proximo
            noAtual.proximo = novoNo
            
    #Funcao pra inserir no inicio
    def inserirNoInicio(self,dado):
        novoNo  = No(dado)
        novoNo.proximo = self.primeiro
        self.primeiro = novoNo
        





    def exibirLista(self):
        noAtual = self.primeiro
        while noAtual is not None:
            print(noAtual.dado, end=" -> ")
            noAtual = noAtual.proximo


lista = listaEncadeada()
lista.inserirNoFim("A")
lista.inserirNoFim("B")
lista.inserirNoInicio("C")
lista.inserirNoInicio("D")




lista.exibirLista()
        
            
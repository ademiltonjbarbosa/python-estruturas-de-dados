# Este codigo representa uma reta numerica e cada Numero é um valor da reta
from numero import Numero

class RetaNumerica:
    def __init__(self):
        self.primeiro = None

    # Funcao que insere numeros no fim da reta

    def inserirNoFim(self, valor):
        novoNumero = Numero(valor)
        if self.primeiro == None:
            self.primeiro = novoNumero
        else:
            auxiliar = self.primeiro
            while auxiliar.proximo is not None:
                auxiliar = auxiliar.proximo
            auxiliar.proximo = novoNumero

    # Funcao que insere no inicio

    def inserirNoInicio(self,valor):
        novoNo = Numero(valor)
        novoNo.proximo = self.primeiro
        self.primeiro = novoNo
     
    # Funcao que exibe a lista Numerica
    def exibirLista(self):
        auxiliar = self.primeiro
        while auxiliar is not None:
            print(auxiliar.valor, end=" - ")
            auxiliar = auxiliar.proximo
        print(" ")

    # Funcao que buscao um valor e retor True caso exista e False caso nao exista
    def buscarNumero(self,valor):
        aux  = self.primeiro
        while aux is not None:
            if aux.valor == valor:
                return True
            else:
                aux = aux.proximo
        return False

    # Funcao que diz o tamanho da lista
    def tamanhoDaReta(self):
        tam = 0
        aux = self.primeiro
        while aux is not None:
            tam +=1
            aux = aux.proximo
        print(f"A lista possui {tam } elementos")                                                                                     
    

    # Funcao que remove elemento da lista
    def removerNumero(self,valor):
        # Testar se a lista esta vazia
        if self.primeiro == None:
            return False
        # Testar se o valor procurado é o primeiro da lista
        if self.primeiro.valor == valor:
            self.primeiro = self.primeiro.proximo
            return True
        
        anterior = self.primeiro
        atual =self.primeiro.proximo
        while atual is not None:
            if atual.valor == valor:
                anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo

        return False
        
      
    # Funcao que diz quem é o maior valor da lista
    def maior(self):
        if self.primeiro == None:
            print("A lista esta vazia")
        else:
            maior = 0
            aux = self.primeiro
            while aux is not None:
                if aux.valor > maior:
                    maior = aux.valor
                    aux = aux.proximo
            print(f"O maior valor da lista é {maior}")
            
    

    

    # Testar se o valor procurado esta no meio da lista



        

lista = RetaNumerica()
# Inserindo no fim
lista.inserirNoFim(5)
lista.inserirNoFim(6)
lista.inserirNoFim(7)
lista.inserirNoFim(8)
lista.inserirNoFim(15)
lista.inserirNoFim(20)
# Inserindo no Inicio
# lista.inserirNoInicio(4)
# lista.inserirNoInicio(3)
# lista.inserirNoInicio(2)
# lista.inserirNoInicio(1)
# lista.inserirNoInicio(17)
# lista.inserirNoInicio(12)
lista.exibirLista()
lista.removerNumero(23)




lista.exibirLista()
# lista.maior()
#print(lista.buscarNumero(9))

#lista.tamanhoDaReta()
# lista.removerNumero(1)
# lista.exibirLista()

    
from letra import Letra

class Alfabeto:
    def __init__(self):
        self.primeiraLetra = None
    
    def inserirLetraNoFim(self,letra):
        novaLetra = Letra(letra)
        if self.primeiraLetra == None:
            self.primeiraLetra = novaLetra
        else:
            letraAtual = self.primeiraLetra
            while letraAtual.proximaLetra is not None:
                letraAtual = letraAtual.proximaLetra
            letraAtual.proximaLetra = novaLetra

    def exibirAlfabeto(self):
        if self.primeiraLetra == None:
            print("Lista Vazia! ")
        else:
            letraAtual = self.primeiraLetra
            while letraAtual is not None:
                print(letraAtual.letra,end=" - ")
                letraAtual = letraAtual.proximaLetra
            print(" ")
    
    def removerLetra(self,letraARemover):
        #Testes: lista esta vazia? - e o primeiro da lista? - esta no meio da lista?
        if self.primeiraLetra is None:
            return False
        if self.primeiraLetra.letra == letraARemover:
            self.primeiraLetra = self.primeiraLetra.proximaLetra
            return True
        
        anterior = self.primeiraLetra
        atual = self.primeiraLetra.proximaLetra

        while atual is not None:
            if atual.letra == letraARemover:
                anterior.proximaLetra  = atual.proximaLetra
                return True
            anterior = atual
            atual = anterior.proximaLetra
        return False

alf1 = Alfabeto()
alf1.inserirLetraNoFim("A")
alf1.inserirLetraNoFim("B")
alf1.inserirLetraNoFim("C")
alf1.inserirLetraNoFim("D")
alf1.inserirLetraNoFim("E")
alf1.inserirLetraNoFim("F")

alf1.exibirAlfabeto()

alf1.removerLetra("C")

alf1.exibirAlfabeto()
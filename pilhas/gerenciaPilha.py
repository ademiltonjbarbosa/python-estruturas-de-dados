from no import No
class GerenciaPilha:
    def __init__(self):
        self.topo = None

    def push(self,valor): # Metodo para inserir valor no topo da pilha
        novoNo = No(valor)
        novoNo.proximo = self.topo
        self.topo = novoNo

    def pop(self): # Remove o valor do topo
        if self.topo is None:
            print("Lista Vazia!")
        else:
            valorTopo = self.topo.valor
            self.topo = self.topo.proximo
            print(f"Voce removeu {valorTopo} do Topo")

    def retornaTopo(self):
        print(self.topo.valor)


pilha1 = GerenciaPilha()
pilha1.push(1)
pilha1.push(2)
pilha1.push(3)
pilha1.push(4)
pilha1.push(5)
pilha1.push(6)

pilha1.retornaTopo()
pilha1.pop()
pilha1.retornaTopo()
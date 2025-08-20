from no import No

class GerenciaFila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileirar(self,valor): # Enqueue, adiciona um valor no fim da fila
        novoNo = No(valor)
        if self.inicio is None:
            self.inicio = novoNo
            self.fim = novoNo
        else:
            self.fim.proximo = novoNo
            self.fim = novoNo

    def desenfileirar(self):
        if self.inicio is None:
            print("Fila Vazia!")
        else:
            valorInicio = self.inicio.valor
            self.inicio = self.inicio.proximo
            return valorInicio
    
    def exibirInicio(self):
        if self.inicio is None:
            print("Lista Vazia!")
        else:
            valorInicio = self.inicio.valor
            return valorInicio
    
fila1 = GerenciaFila()
fila1.enfileirar(1)
fila1.enfileirar(8)
fila1.enfileirar(3)
fila1.enfileirar(4)
fila1.enfileirar(5)

print(fila1.exibirInicio())
excluir = fila1.desenfileirar()
print(fila1.exibirInicio())
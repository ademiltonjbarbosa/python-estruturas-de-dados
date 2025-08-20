from cliente import Cliente

class FilaIngresso:
    def __init__(self):
        self.primeiro = None

    def inserirNoFim(self,nomeCliente):
        novoCliente = Cliente(nomeCliente)
        if self.primeiro == None:
            self.primeiro =novoCliente
        else:
            aux = self.primeiro
            while aux.proximo is not None:
                aux = aux.proximo
            aux.proximo = novoCliente

    def inserirNoInicio(self,nomeCliente):
        novoCliente = Cliente(nomeCliente)
        novoCliente.proximo = self.primeiro
        self.primeiro = novoCliente

    def exibirListaClientes(self):
        aux = self.primeiro
        while aux is not None:
            print(aux.nome,end="--")
            aux = aux.proximo
        print(" ")

    #Funcao que em teoria remove o cliente da fila
  
        
 

# INserindo clientes no final da lista 
filaCliente1 = FilaIngresso()
filaCliente1.inserirNoFim("Maria")
filaCliente1.inserirNoFim("Laura")
filaCliente1.inserirNoFim("Edna")
filaCliente1.inserirNoFim("Sandra")
filaCliente1.inserirNoFim("Alvaro")

# Exibindo a lista de Clientes
filaCliente1.exibirListaClientes()

filaCliente1.inserirNoInicio("Sr. José")
filaCliente1.exibirListaClientes()


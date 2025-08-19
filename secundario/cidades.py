#Classe Cidade, cada objeto Cidade criado sera um Nó.
class Cidade:
    def __init__(self,cidade):
        self.cidade = cidade
        self.proxCidade = None

#"Criando" os objetos do tipo cidade, a principio todos possuem seus proximos sendos vazios
cdd1 = Cidade("Valenca")
cdd2 = Cidade("Taperoa")
cdd3 = Cidade("Salvador")
cdd4 = Cidade("Ilheus")

# Atribuindo proximo para cada Objeto.
cdd1.proxCidade = cdd2
cdd2.proxCidade = cdd3
cdd3.proxCidade = cdd4

cidadeAtual = cdd1
while cidadeAtual is not None:
    print(cidadeAtual.cidade)
    cidadeAtual = cidadeAtual.proxCidade
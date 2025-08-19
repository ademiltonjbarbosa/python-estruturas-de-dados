class No:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None


no1 = No("A")
no2 = No("B")
no3 = No("C")

no1.proximo = no2
no2.proximo = no3

# print(no1.dado)
# print(no1.proximo)
# print(no2.proximo)

atual = no1
while atual is not None:
    print(atual.dado)
    atual = atual.proximo
    
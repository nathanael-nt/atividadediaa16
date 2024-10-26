class Vendedor:
    def __init__(self, nome, nome2):
        self.nome = nome
        self.nome2 = nome2

    def informacaoSaida(self):
        print(f'Olá, meu nme é ',self.nome, 'e eu tenho')

vendedor1 = Vendedor(input('Nome 1: '),input('Sobrenome 2 '))
vendedor2 = Vendedor(input('Nome 1: '),None)

vendedor1.informacaoSaida()
vendedor2.informacaoSaida()
 
#  1

class Pessoa:
    def __init__(self, nome, sobrenome, idade, cidade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade

nomee = input("Qual o seu nome? ")
sobrenomee = input("Qual é o seu sobrenome? ")
idadee = int(input("Qual sua idade? "))
cidadee = input("Qual sua cidade? ")

pessoa1 = Pessoa(nomee, sobrenomee, idadee, cidadee)

print(f"\nnome: {pessoa1.nome}\nsobrenome: {pessoa1.sobrenome}\nidade: {pessoa1.idade}\ncidade: {pessoa1.cidade}")
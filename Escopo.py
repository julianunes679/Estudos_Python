def saudacao():
    print("Olá, Júlia. Bem vinda ao Python")
saudacao()


numeros = [1, 2, 3]
numeros.append(6)  # adiciona um item
print(numeros)


### Escopo

x = 10
def minha_funcao():
    x = 5
    print ("dentro:", x)

minha_funcao()
print ("fora:", x)


### Global
contador = 2

def incrementa():
    global contador 
    contador += 1

incrementa()
print(contador)


### Nonlocal

def externa():
    mensagem = "Olá, Júlia!"
    
    def interna():
        print(mensagem)  # pode usar a variável da função externa
    
    interna()

externa()

def externa():
    contador = 0
    
    def interna():
        nonlocal contador   # diz: "essa variável vem da função de fora"
        contador += 1
        print("Contador:", contador)
    
    interna()

externa()


### Escopo em Metodos (Classe)

class Conta:
    def __init__(self, dono, saldo):
        self.dono = dono
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor  # acessa o escopo da instância
        print(f"Depósito de R${valor} feito. Saldo atual: R${self.saldo}")

    def mostrar(self):
        print(f"Dono: {self.dono}, Saldo: {self.saldo}")

conta1 = Conta("Júlia", 100)
conta1.depositar(50)
conta1.mostrar()

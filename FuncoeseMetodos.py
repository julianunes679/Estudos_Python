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

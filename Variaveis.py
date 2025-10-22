#variaveis básicas 
nome = "Júlia"                     # texto (string)
idade = 20                         # numero inteiro (int)
altura = 1.69                      # numero decimal (float)
estudando = True                   # valor logico (bool)

print (nome)
print (idade)
print (altura)
print (estudando)

###########

print (type(nome))

###########

idade = 18

if idade >= 18:
    print ("você é maior de idade")
else:
    print ("você é menor de idade")

############

nota = float (input("Digite sua nota aqui"))

if nota >= 7:
    print ("Você está aprovado")
elif nota >= 5:
    print ("Você está de recuperação")
else:
    print ("Você está reprovado") 
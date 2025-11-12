class Conta:
    def __init__(self, dono, saldo):
        self.dono = dono        # público
        self._tipo = "Corrente" # protegido
        self.__saldo = saldo    # privado

    def mostrar_saldo(self):
        print(f"Saldo: R${self.__saldo}")

conta = Conta("Júlia", 500)

print(conta.dono)       #Acesso permitido
print(conta._tipo)      #Acesso possível, mas NÃO recomendado
print(conta.__saldo)    #ERRO: atributo privado


### Getters e Stters 

class Conta:
    def __init__(self, dono, saldo):
        self.__saldo = saldo
        self.dono = dono

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido")

    def ver_saldo(self):
        return self.__saldo

conta = Conta("Júlia", 100)
conta.depositar(50)           ### método setter (modifica com segurança)
print(conta.ver_saldo())      #150 método getter (mostra o valor sem expor diretamente)


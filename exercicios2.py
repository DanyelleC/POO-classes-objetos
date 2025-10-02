#1-Crie uma classe Usuario com atributos nome e email. Depois, crie uma classe Cliente que herde de Usuario. 
#Crie uma instancia de um cliente e acesse todos os atributos.
class Usuario:
    def _init_(self,nome,email):
        self.nome = nome
        self.email = email
    def __str__(self):
        return ("O cliente {self.nome} obtém o email: {self.email}")
class Cliente(Usuario):
    pass

cliete1 = Cliente("Danyelle", "danyelle031199@gmail.com")
cliente1.nome
cliente1.email



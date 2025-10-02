from abc import ABC, abstractmethod

class Pessoa (ABC):
    @abstractmethod
    def falar(self):
        pass

    @abstractmethod
    def andar(self):
        pass

    @abstractmethod
    def comer(self):
        pass

# class Funcionario(Pessoa):
#     def falar (self):
#         return super().falar()
#     def andar (self):
#         return super().andar()
#     def comer(self):
#         return super().comer()

class Funcionario(Pessoa):
    @abstractmethod
    def falar (self):
        print (" O Funcionario está falando")
    
    @abstractmethod
    def andar (self):
        print ("O funcionario está andando")
    
    @abstractmethod
    def comer(self):
        print ("O funcionario está comendo")

    
class Aluno (Pessoa):
    @abstractmethod
    def falar (self):
        print ("O aluno está falando")
    
    @abstractmethod
    def andar (self):
        print ("O aluno está andando")

    @abstractmethod
    def comer(self):
        print ("O aluno está comendo")
    

f = Funcionario()
a = Aluno()

    
print (f.falar())
print (f.andar())
print (f.comer())

print (a.falar())
print (a.andar())
print (a.comer())


#2
from abc import ABC, abstractmethod

class Pessoa (ABC):
    @abstractmethod
    def falar(self):
        pass

    @abstractmethod
    def andar(self):
        pass

    @abstractmethod
    def comer(self):
        pass

class Funcionario(Pessoa):
    @abstractmethod
    def falar (self):
        print (" O Funcionario está falando")
    
    @abstractmethod
    def andar (self):
        print ("O funcionario está andando")
    
    @abstractmethod
    def comer(self):
        print ("O funcionario está comendo")

    
class Aluno (Pessoa):
    @abstractmethod
    def falar (self):
        print ("O aluno está falando")
    
    @abstractmethod
    def andar (self):
        print ("O aluno está andando")

    @abstractmethod
    def comer(self):
        print ("O aluno está comendo")
    

f = Funcionario()
a = Aluno()

    
# for pessoa in [f,a]:
#     print (pessoa.falar())
#     print (pessoa.comer())
#     print (pessoa.andar())
#     print ("-" * 40)



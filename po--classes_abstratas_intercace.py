#Tem mais informações













from abc import ABC, abstractmethod
class Pessoa (ABC):
    @abstractmethod
    def comer (self):
        print ("A pessoa esta comendo")
    @abstractmethod
    def andar(self):
        print("A pessoa esta andando")
        @abstractmethod
    def correr (self):
        print ("A pessoa esta correndo")

class Estudante (Pessoa):
    def comer (self):
        return super ().comer()
    def andar (self):
        return super().andar()
    def correr(self):
        return super().correr()
    
joao = Estudante()
joao.andar()
joao.correr()
joao.comer()

from abc import ABC, abstractmethod

class Animal (ABC):
    @abstractmethod
    def movimentar (self,metros:float):
        ...

class Cachorro (Animal):
    def movimentar (self, metros):
        print (f"O cachorro andou {metros} metros")

dog = Cachorro ()
dog.movimentar(4.5)




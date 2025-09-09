# #_init_

# #_str_

# class Cachorro:
#     especie = "Canis lupus familiaris"

# def _init_ (self,nome,raca, idade):
#     self.nome = nome
#     self.raca = raca
#     self.idade = idade

# def _str_ (self):
#     return f"especie { self.especie}\nNome: {self.nome}\nRaça: {self.raca}\nIdade: {self.idade}"
# doguinho01 = Cachorro ("Rex","caramelo",2)
# print (doguinho01)


# #Adicionando métodos

# class Cachorro:
#     especie = "Canis Lupus familiaris"
#     def _init_ (self,nome: str, idade: int, raca:str="caramelo"): #Método
#         self.nome = nome
#         self.idade = idade 
#         self.raca = raca

#         def _str_(self):
#             return f"Especie: {self.especie}\nNome: {self.nome}\nRaça: {self.raca}\nIdade: {self.idade}"
#         def latir (self):
#             print("Au Au Au ")

#             def correr (self,metros):
#                 print(f"{self.nome} correu{metros}m")
        
# auau1 = Cachorro ("Bob",15)
# auau1.latir()
# auau1.correr(50)







class ContaBancaria:
    def _init_ (self,nome,numero_conta,saldo):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.operacoes = []

    def _str_ (self):
        return f"Conta nº{self.numero_conta}do titular {self.nome}"
    
    def registro_operacoes(self,tipo, valor):



    def saque(self,valor):
        if valor > self.saldo:
            print("Saldo Insuficiente")
        else:
            self.saldo -= valor
            self.operacoes.append (["saque",valor])



    def deposito (self,valor):
        self.saldo += valor
        self.operacoes.append (["saque",valor])
    
    def extrato (self):
        for operacao in self.operacoes:
            print (operacao)



    conta1 = ContaBancaria ("Frederico", 321425)
    conta2 = ContaBancaria ("Gleibson", 325245,4235245)
  
    print (conta1)
    print (conta2)


    conta1.deposito (500)
    conta2.saque (500)
    print(conta1)
    print(conta2)
    print (conta1.operacoes)




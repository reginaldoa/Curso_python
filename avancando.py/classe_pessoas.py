#Criar classes com o tema "pessoas"



class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome 
        self.idade = idade
        self.cargo = cargo


    def informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Nome: {self.idade}")
        print(f"Nome: {self.cargo}")

    def promover(self, novo_Cargo):
        print(f"{self.nome} foi promovido(a) para a nova função de {novo_Cargo} ")
        #self.cargo = novo_Cargo

    def atualizar_idade(self, nova_idade):
        if nova_idade > self.idade:
            print(f"A nova idade da {self.nome} é de {self.idade} para {nova_idade}")
        else:
            print(f"A nova idade tem que ser maior que a anterior.")


funcionario_1 = Pessoa("Reginaldo" , 30 , "Analista de dados")
funcionario_2 = Pessoa("Thiago", 28 ,"Logistica")
  

print('\nColaborador 1:')
funcionario_1.informacoes()
funcionario_1.promover("Cientista de dados")
funcionario_1.atualizar_idade(31)

print('\nColaborador 2:')
funcionario_2.informacoes()
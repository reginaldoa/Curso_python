#Chamar as funções do arquivo funcoes.py
from  funcoes import saudacao, somar, teste, verificar_maioridade


print(saudacao("Reginaldo"))
somar(2,10)
teste()

sua_idade = int(input("Digite a sua idade, por favor:"))

if verificar_maioridade(sua_idade): 
    print("Você é maior de idade")
else:
    print("Você é menor de idade.")

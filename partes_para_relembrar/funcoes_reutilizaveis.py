# Funções

#Sintaxe

def saudacao(nome, idade):
    print(f"Olá {nome}! Vamos aprender  AI? PQ você tem {idade} anos")
    

saudacao("reginaldo",30)


def somar(x,y):
    return x + y

resultado = somar(2,5)
print(f"O resultado da soma é: {resultado}")


def calcular_porcentagem(preco , porcentagem):
    return preco - (preco * porcentagem / 100)


valor_final = calcular_porcentagem(100,20)
print(f"O valor final com desconto é de R${valor_final:.2F}")



def aluno_passou(n1 , n2 , n3 , n4):
    return (n1 + n2 + n3 + n4) / 4


resultado1 = int(input("Digite as notas:"))
resultado2 = int(input("Digite as notas:"))
resultado3 = int(input("Digite as notas:"))
resultado4 = int(input("Digite as notas:"))

resultado = aluno_passou(resultado1 , resultado2, resultado3,resultado4 )

if resultado > 5:
    print("Passou")
elif resultado < 5 :
    print("Reprovou")
else:
    print("Recuperação")
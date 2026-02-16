#falando sobre loops

#O for é utilizado quando sabemos a quantidade de vezes que preciso repetir a tarefa

#O while utilizamos quando não sabemos a quantidade de vezes que precisamos repetir a tarefa, vai depender de uma condição



for x in range(11,1,-2):
    print(x)


quantidade = 10
x=1

while x <= quantidade:
   print(x)
   x += 1 



# senha com while


senha  = input("Digite a sua senha:")


while senha != "reginaldo":
    print("Você está digitando a senha errada. Digite novamente")
    senha = input("Qual é a senha?")

print("Acesso permitido")
#Quando utilizo uma lista? Quando preciso de um ou vários itens mutáveis
#Tuplas = um ou vários itens imutáveis
#Dicionarios = são listas com "esteróides"! Utilizamos quando precisamos armazenar um item relacionado a uma chave

#LISTA
frutas = ["banana" , "maça", "laranja"]

#print(frutas[2])

#add = input("Qual fruta vc deseja adcionar?")

#frutas.append(add)
frutas.remove("banana")

#print(len(frutas))


tarefas = []

tarefas.append("Estudar python com IA")
tarefas.append("Ler um artigo sobre IA")
tarefas.append("Responder e-mails")
tarefas.append("Reginaldo")

#print("Minhas tarefas diárias:")
#print(tarefas[0])
#print(tarefas[1])
#print(tarefas[2])

numero = 0

print("Minhas tarefas diárias de hoje:")
for tarefas in tarefas:
    numero += 1
    print(f"Tarefa número {numero}:{tarefas}")
    
    

print("Concluído!!")


#TUPLE
meses = ("Janeiro", "Fevereiro","março")
print(meses)
print(meses[0])





#DICIONÁRIOS
usuario =  {
    "nome": "Reginaldo",
    "Sexo": "Masculino",
    "idade": 30 , 
    "signo": "Escorpião",
    "Departamento" : "TI"
}

#print(usuario["nome"])
#print(usuario["idade"])

usuario["nome"] = "Reginaldo Alves da Silva"
usuario["Cidade"] = "São Paulo"

print(usuario)



aluno ={
    "nome"  : input("Nome do aluno:"),
    "idade" : int(input("Idade do aluno:")),
    "nota"  : float(input("Nota do aluno:"))
}

print(f"O aluno {aluno["nome"]} tem {aluno["idade"]} anos e tirou a nota: {aluno["nota"]}")
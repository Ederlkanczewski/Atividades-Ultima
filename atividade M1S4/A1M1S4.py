clientes = [] #Lista de Clientes

for cliente in range(5):
  nome = input()
  cpf = input()
  idade = int(input())
  
  cadastro_atual = {}
  cadastro_atual["Nome"] = nome
  cadastro_atual["CPF"] = cpf
  cadastro_atual["Idade"] = idade
  clientes.append(cadastro_atual)
  
for cliente in clientes :
  print("Cliente:", cliente["Nome"], "CPF:", cliente["CPF"], "Idade:", cliente["Idade"])
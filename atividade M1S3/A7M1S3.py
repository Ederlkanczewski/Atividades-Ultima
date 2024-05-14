def conta_letras(letra_buscada, frase):
  contagem = 0 #Inicia a contagem a partir do zero
  for letra_atual in frase :
    if letra_atual == letra_buscada:
     contagem += 1
  return contagem

letra = input()
frase = input()
saida = conta_letras(letra, frase)
print(saida)
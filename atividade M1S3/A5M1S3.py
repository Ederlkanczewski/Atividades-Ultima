def positivo_negativo_zero(numero):
  if numero == 0:
    return "Zero"
  elif numero > 0:
    return "Positivo"
  else:
    return "Negativo"

numero = int(input())
print(positivo_negativo_zero(numero))
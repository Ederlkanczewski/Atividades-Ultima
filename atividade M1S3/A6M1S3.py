def gorjeta(valor, porcentagem):
  return valor*porcentagem/100

valor_conta = float(input())
porcentagem = int(input())
resultado = gorjeta(valor_conta, porcentagem)
print(f"{resultado:.2f}")
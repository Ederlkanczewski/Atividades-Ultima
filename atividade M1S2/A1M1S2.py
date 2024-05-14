horas_estimadas = 80
valor_inicial = 1000.00
valor_hora = 20.45
taxa = 0.15
valor_total = (valor_inicial + horas_estimadas * valor_hora) * (1 + taxa)
valor_total = round(valor_total, 2)
print(f'{valor_total:.2f}')
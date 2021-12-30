valor = float(input('Qual é o valor do produto? '))
desconto = (valor * 5)/100
valorD = valor - desconto
print('O produto que custava R${} com 5% de desconto ficará R${}'.format(valor,valorD))
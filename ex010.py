print('=='*10)
print('Vamos converter seus reais em dólars ')
real = float(input('Quanto de dinheiro você quer trocar?   '))
dolar = 5.79
troca = real/dolar
print('Com R$ você receberá U${:.2f}'.format(troca))
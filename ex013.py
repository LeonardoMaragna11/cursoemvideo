s = float(input('Qual é o valor do salário?  '))
reajuste = (s * 15)/100
snovo = s + reajuste
print('O funcionário que recebia R${:.2f} agora receberá R${:.2f} '.format(s,snovo))
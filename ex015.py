dias = int(input('Quantos dias voê alugou o carro? '))
kmr = float(input('Quantos km foram rodados? '))
pdias = 60
pkmr = 0.15
valor = (kmr * pkmr) + (pdias * dias)
print('O total a pagar é de R${}'.format(valor))
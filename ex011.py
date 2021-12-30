altura = float(input('Qual é a altura da parede em metros? '))
largura = float(input('Qual é a largura da parede em metros? '))
area = altura * largura
tinta1l = 2
quantidadedetinta = area/tinta1l
print('A sua parede tem {}m² entao será necessário usar {}Litros de tinta'.format(area,quantidadedetinta))
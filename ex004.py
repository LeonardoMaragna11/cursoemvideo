algo = input('Digite qualquer coisa: ')
print('O tipo primitivo é {}'.format(type(algo)))
print('So tem espaços? ', algo.isspace())
print('É númerico? ', algo.isalnum())
print('É afabético? ', algo.isalpha())
print('É alfanúmerico? ', algo.isalnum())
print('É composto por letras maiúsculas? ', algo.isupper())
print('É composto por letras minúsculas? ', algo.islower())
print('É capitalizado? ', algo.istitle())

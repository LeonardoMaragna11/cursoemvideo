from random import shuffle
times_alternativos = ['Porto', 'Benfica', 'Brugge', 'Sporting']
shuffle(times_alternativos)
t1 = 'Vasco'
t2 = 'Botafogo'
t3 = 'Goias'
t4 = times_alternativos[0]
times = [t1, t2, t3, t4]
shuffle(times)
print(times[0], ' X ', times[1])
print(times[2], ' X ', times[3])

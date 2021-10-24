# промежуток времени
duration = int(input('Введите промежуток времени в секундах: '))
m1 = 60
h1 = m1 ** 2
d1 = h1 * 24
d = duration // d1
h = (duration - d * d1) // h1
m = (duration - h * h1 - d * d1) // m1
s = duration % m1
print(d, 'дн.', h, 'ч.', m, 'мин.', s, 'сек.')


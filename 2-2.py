elem = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
num = len(elem)
print(num)
print(elem)
print((' '.join(elem)).isdigit)

s = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(s):
    if s[i].isdigit() or s[i] == '+5':
        if len(s[i]) == 1:
            s[i] = '0' + s[i]
        if s[i] == '+5':
            s[i] = '+05'
        s.insert(i, ' " ')
        s.insert(i + 2, ' " ')
        i += 2
    else:
        i += 1
print(s)

new_string = ''

i = 0
while i < len(s):
    if s[i] == ' " ' and (s[i + 1] == '05' or s[i + 1] == '+05' or s[i + 1] == '17') and s[i + 2] == ' " ':
        new_string += '"' + s[i + 1] + '" '
        i += 2
    else:
        new_string += s[i] + ' '
    i += 1
print(new_string)

prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01,
          63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29, 8.53, 67, 95,
          5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
# a
for elem in prices:
    number = str(float(elem))
    pos = number.find(".")
    r = int(number[:pos])
    k = number[pos + 1:]
    if len(k) == 2 and k[0] == '0':
        print(str(r) + " руб. " + str(k[0]) + str(k[1]) + "коп.")
    elif len(k) == 2 and k[0] != '0':
        print(f"{r} руб. {int(k)} коп.")
    elif len(k) == 1:
        print(f"{r} руб. {k}0 коп.")

# b
increase = sorted(prices)
print(id(increase), increase)
increase.reverse()
print(id(increase), increase)

# c
decrease = sorted(prices, reverse=True)
print(id(decrease), decrease)

# c
print(sorted(prices, reverse=True)[:5])

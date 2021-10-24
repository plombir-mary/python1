# склонение слова процент
for i in range(0, 235):
    if i == 11 or i == 12 or i == 13 or i == 14 or i == 111 or i == 112 or i == 113 or i == 114 or i == 211 or i == 212 or i ==213 or i ==214:
        print(f"{i} процентов")
    else:
        if i % 10 == 1:
            print(f"{i} процент")
        elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
            print(f"{i} процента")
        else:
            print(f"{i} процентов")

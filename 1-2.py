a = [i ** 3 for i in range(1, 1001) if i % 2 != 0]

# a
global_sum = 0
for elem in a:
    n = elem
    local_sum = 0
    while n > 0:
        digit = n % 10
        local_sum = local_sum + digit
        n = n // 10
    if local_sum % 7 == 0:
        global_sum += elem
print(global_sum)

# b;с
global_sum = 0
for elem in a:
    elem += 17
    n = elem
    local_sum = 0
    while n > 0:
        digit = n % 10
        local_sum = local_sum + digit
        n = n // 10
    if local_sum % 7 == 0:
        global_sum += elem
print(global_sum)

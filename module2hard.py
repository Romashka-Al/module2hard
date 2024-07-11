a = int(input("Число из первой вставки: "))
result = ''
for i in range(1, a + 1):
    for j in range(i + 1, a + 1):
        if a % (i + j) == 0:
            result += f'{i}{j}'
print(a, '-', result)
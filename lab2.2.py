n = int(input('Введите число: '))
result = n
first_value = int(str(result)[0])
while first_value and first_value != 1 and result < 1000000000:
    result *= first_value
    first_value = int(str(result)[0])
print('Результат =', result)

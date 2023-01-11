# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
koefs = []
k = int(input("Введите степень многочлена k: "))
for i in range(k + 1):
    num = randint(0, 100)
    koefs.append(num)

result = ''
for i in range(len(koefs)):  # for i, koef in enumerate(koefs):
    if len(result) > 0 and koefs[i] > 0:
        result = result + '+'
    if koefs[i] == 0:
        continue
    result = result + str(koefs[i]) + 'X^' + str(k - i)
if koefs[-1] != 0:
    result = result[:len(result) - 3]
result = result + ' = 0'
print(result)

with open('TASK1.txt', 'w', encoding='utf-8') as my_file:
    my_file.write(result)

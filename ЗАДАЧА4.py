# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



from random import randint
from sympy import symbols
from math import prod

max_val = 100
k = int(input('Введите натуральную степень:'))
factor = [randint(-max_val, max_val) for i in range(k)]+[randint(1, max_val)]
x = symbols('x')
result = sum(map(prod,zip(factor,[x**i for i in range(k+1)])))# Применим широкий комплекс встроенных функций для получения результата в одну строку
print(f'{result} = 0')
# Произведём запись решения в указанный файл
with open('ЗАДАЧА4.txt', 'w') as my_file:
    my_file.write(f'{result} = 0')


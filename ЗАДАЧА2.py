# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = int(input('Введите натуральное число: '))
lst = []
x = 2
while x * x <= N:
    if N % x == 0:
        lst.append(x)
        N = N // x
    else:
        x = x + 1
if N >= 1:       
    lst.append(N)
print(lst)
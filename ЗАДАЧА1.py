# Вычислить число пи c заданной точностью d
#from cmath import pi
#import math
#print(round(math.pi, 2))

import math
N = int(input("Введите количество цифр после запятой:"))
print("Число 𝜋: {:.45f}".format(math.pi))
x  = math.pi
y = round(x,N+1)*10**N
z = math.modf(y)
x = z[1] / 10**N
print("Число 𝜋 с заданной точностью:", x)
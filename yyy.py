import math as m

def ff(x):
    f1 = m.pow(x - 4, 3) + m.log(x, m.e)
    f2 = abs(x + m.cos(x) / m.asin(x))
    f3 = m.pow(m.cos(x + 2), 3)
    F = f1 / f2 + f3
    return F

x = int(input("x = "))
print(ff(x))
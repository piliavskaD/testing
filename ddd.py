import math

def ff(d1, d2):
    if d1 > 10 and d2 > 10:
        return "nnn"
    else:
        return 0.5 * d1 * d2

d1 = int(input("d1 = "))
d2 = int(input("d2 = "))
print(ff(d1, d2))
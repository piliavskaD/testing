import math 

def ff(x):
    if x >= 1:
        f = 7 * math.log(x, math.e) + math.log(x, 7) + math.log(x, 10)
        return f
    elif -10.3 < x < 1:
        f = math.sin(x) - math.cos(x + 2 + math.pi / 7)
        return f
    elif x <= -10.3:
        f = 2.24 * math.pow(math.e, 0.5 * x + 0.1) * math.pow(2, 0.3 * x)
        return f
    
x = int(input("x = "))
print(ff(x))
import math

def ppl(a):
    f = int(str(a)[0])
    s = int(str(a)[1])
    t = int(str(a)[2])
    fr = int(str(a)[3])
    if f * s * t * fr >= 0:
        return math.sqrt(f * s * t * fr)
    else:
        return "err"
    
a = int(input("a ="))
print(ppl(a))
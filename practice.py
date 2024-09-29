import math

def cal(x1, y1, x2, y2):
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

Mx = int(input("Mx "))
My = int(input("My "))


ax = int(input("ax = "))
ay = int(input("ay = "))
bx = int(input("bx = "))
by = int(input("by = "))
cx = int(input("cx = "))
cy = int(input("cy = "))

dist_A = cal(Mx, My, ax, ay)
dist_B = cal(Mx, My, bx, by)
dist_C = cal(Mx, My, cx, cy)

final = max((dist_A, "A"), (dist_B, "B"), (dist_C, "C"))[1]
print(final)




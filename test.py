def ff(a):
    r = int(str(a)[0]) - int(str(a)[2])
    return r

while True:
    a = int(input("a = "))
    if len(str(a)) == 3:
      break
    else:
      print("repeat")

#dd = ff(a)
print(ff(a))
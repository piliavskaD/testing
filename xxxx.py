def ppl(a, b):

    third1 = int(str(a)[2])
    third2 = int(str(b)[2])
    return third1 + third2, third2 * third1
a = int(input("a = "))
b = int(input("b = "))
print(ppl(a, b))
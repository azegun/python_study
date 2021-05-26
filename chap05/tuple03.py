a, b =10, 20

print("a :", a, "b :", b, end="\n\n")

a, b = b, a
print("a : ", a, "b :", b, end='\n\n')

def test():
    return (10, 20)

a, b = test()
print("a: ", a, "b: ", b, end = '\n\n')

def f(x):
    return 2 * x+1

print(f(10))

def f(x):
    return x ** 2 + 2 * x +1
print(f(10))


def mul(*values):

   output =1
   for value in values:
       output *= value
   return output

print(mul(5, 7, 9, 10))
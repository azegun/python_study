dictionary = {
    1: 1 ,
    2: 1
}

def fibonacci(n):
    # dictionary에 들어있는 key가 있다면,
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output
    

print("fibonacci(1):", fibonacci(10))
print("fibonacci(1):", fibonacci(20))
print("fibonacci(1):", fibonacci(30))
print("fibonacci(1):", fibonacci(40))
print("fibonacci(1):", fibonacci(50))
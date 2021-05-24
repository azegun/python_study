# def factorial(n):
#     output = 1
#
#     for i in range(1, n+1):
#         output *= i
#     return output
#
# print("1!:", factorial(1))
# print("2!:", factorial(2))
# print("3!:", factorial(3))
# print("4!:", factorial(4))
# print("5!:", factorial(5))
#
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print("1!:", factorial(1))
# print("2!:", factorial(2))
# print("3!:", factorial(3))
# print("4!:", factorial(4))
# print("5!:", factorial(5))

counter = 0

def fibonacci(n):

    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1

    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(10)
print("---")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))
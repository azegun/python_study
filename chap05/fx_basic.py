# def print3_times():
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")
#
# print3_times()
#
# print()
# def print_n_tiems(value, n):
#     for i in range(n):
#         print(value)
#
# print_n_tiems("안녕하세요", 5)
#
# def print_n_times1(n, *values):
#
#     for i in range(n):
#         for value in values:
#             print(value)
#
#         print()
#
# print_n_times1(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")
#
# def print_n_times2(value, n=2):
#     for i in range(n):
#         print(value)
#
# print_n_times2("안녕하세요")
def print_n_times(*values, n=2):

    for i in range(n):
        for value in values:
            print(value)

        print()

print_n_times("안녕하세여", "즐거운", "파이썬 프로그래밍", 3)

def test(a, b=10, c=100):
    print(a + b + c)

# 기본 형태
test(10, 20, 30)

#키워드 매개변수로 모든 매개변수를 지정한 형태
test(a = 10, b = 100, c = 200)

#키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
test(c =10, a = 100, b = 200)

#키워드 매개변수로 일부 매개변수만 지정한 ㅕㅎㅇ태
test(10, c=200)

def return_test():
    print("A 위치입니다.")
    return
    print("B 위치입니다.")

return_test()

def return_test1():
    return 100

value = return_test1()
print(value)

def return_test2():
    return

value = return_test2()
print(value)


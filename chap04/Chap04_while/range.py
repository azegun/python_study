# for i in range(5):
#     print(str(i), "= 반복 변수")
# print()
#
# for i in range(5, 10):
#     print(str(i), "= 반복 변수")
# print()
#
# for i in range(0, 10, 3):
#     print(str(i), "= 반복 변수")
# print()
#
# array = [273, 32, 103, 57, 52]
#
# for i in range(len(array)):
#     print("{}번쨰 반복 : {} ".format(i, array[i]))
#

for i in range(5, -1, -1):
    print("현재 반복 변수 : {}".format(i))

print()

for i in reversed(range(5)):
    print("현재 반복 변수 : {}".format(i))
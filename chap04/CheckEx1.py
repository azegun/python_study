numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]


#2번문제
for number in numbers:
     if(number > 100):
        print(" - 100 이상의 수 :", number)

# 3-1번문제
# for number in numbers:
#     if(number % 2 ==0):
#         print(number,"는 홀수입니다.")
#     else:
#         print(number,"는 짝수입니다.")
#
# print()
 # 3-2번문제
for number in numbers:
     print(number, "는", len(str(number)), "자릿수입니다.")
#     if(i < 10):
#         print(i, "는 1자릿수입니다.")
#     elif(i < 100):
#         print(i, "는 2자릿수입니다.")
#     else:
#         print(i, "는 3자릿수입니다.")

#4번 문제
# list_of_list = [[1,2,3], [4,5,6,7], [8,9]]
#
# for sub_list in list_of_list:
#     for i in sub_list:
#         print(i)

#5번 문제
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# output = [[], [], []]
#
# for number in numbers:
#     output[(number + 2) % 3].append(number)
#
# print(output)
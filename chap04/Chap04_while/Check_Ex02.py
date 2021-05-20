# 2번문제
# key_list = ["name", "hp", "mp", "level"]
# value_list = ["기사", 200, 30, 5]
# character = {}
#
# for i in range(len(key_list)):
#     character[key_list[i]] = value_list[i]
#
# print(character)

limit = 10000
i = 1

sum_value = 0

# if sum_value < limit:
#     for i in range(su):
#         sum_value += i
#         i += 1

while sum_value < limit:
    sum_value += i
    i += 1

print("{}를 더할 떄 {}를 넘으며 그떄의 값은 {}입니다.".format(i-1, limit, sum_value))

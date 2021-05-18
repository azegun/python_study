# list_a = [1, 2, 3]
#
# print("# 리스트 뒤에 요소 추가하기")
# list_a.append(4)
# list_a.append(5)
# print(list_a)
# print()
#
#
# print("# 리스트 중간에 요소 추가하기")
# list_a.insert(0, 10)
# print(list_a)
#
# list_b = [1, 2, 3]
# print("# extend()")
# list_b.extend([4, 5, 6])
# print(list_b)

list_a = [1, 2, 3]
list_b = [4, 5, 6]

print(list_a + list_b)

print(list_a)
print(list_b)

print()

list_a.extend(list_b)
print(list_a)
print(list_b)
list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")
#제거 방법[1] - del
del list_a[1]
print("del list_a[1] : ", list_a)

#제거 방법[2] - pop()
list_a.pop(2)
print("pop(2): ", list_a)

print()

#제거 - del
list_b = [0, 1, 2, 3, 4, 5, 6]
del list_b[3:6]
print(list_b)

list_c = [0, 1, 2, 3, 4, 5, 6]
del list_c[:3]
print(list_c)

print()

#제거 remove(값) - 첫번쨰 값

list_d = [1, 2, 1, 2]
list_d.remove(2)
print(list_d)
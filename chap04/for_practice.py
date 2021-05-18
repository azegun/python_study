list_a = [273, 32, 103, "문자열", True, False]
list_b = [i for i in list_a]
print(type(list_b), list_b)

#1~ 100까지 짝수만 출력
even_list = [i for i in range(101) if i % 2 ==0]
print(even_list)

# 1~ 100까지 홀수만 출력
odd_list = [i for i in range(101) if i % 2 != 0]
print(odd_list)

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
numberTo100 = [i for i in numbers if i >= 100]
print("100이상의 수", numberTo100)

# 숫자 하나씩 다 출력
list_of_list = [[1, 2, 3], [4, 5, 6, 7], [8,9]]
for sub_list in list_of_list:
    for i in sub_list:
        print(i)

#list로 다시 넣어서 출력
list_seq = [i for sub_list in list_of_list for i in sub_list]
print("list_seq", list_seq)

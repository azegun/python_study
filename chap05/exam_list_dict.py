list_a = [[10, 20], [30, 40, 70, 110], [50, 60], [80, 90, 100]]
dict_b = {'k': {'a': 10, 'b': 20}, 'l': {'a': 10, 'b': 20, 'c': 40}, 'm': {'a': 10}}

for key in dict_b:
    if type(dict_b[key])is dict:
        print(key, "->", end='\t')
        for small_key in dict_b[key]:
            print( small_key, ":", dict_b[key][small_key], end='\t')
        print()




for i in list_a:
    print()
    for j in i:
        print(j, end="\t")

print()
print()

# 리스트로 다시 넣기
list_num = [j for i in list_a for j in i]
print(type(list_num), list_num)


# for i in list_a:
#     print(i)
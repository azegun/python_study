output1 =[i for i in range(1, 100+1) if "{:b}".format(i).count("0") == 1]

for i in output1:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계 :", sum(output1))


# print()
# output2 =[i for i in range(1, 101) if "{:b}".format(i).count("0") == 1]
# for i in output2:
#     print("{} : {}".format(i, "{:b}".format(i)))
# print("합계 :", sum(output2))
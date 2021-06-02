def dan(num):
    for i in range(1, 10):
        print('{} * {} = {:2}'.format(num, i, num * i), end="\t")
        # print('{0} * {1} = {2:2}'.format(num, i, num * i))

def gugudan():
    for i in range(1, 10):
        dan(i)
        print()



if __name__ == "__main__":
    gugudan()
# def gugudan2():
#     for j in range(1, 10):
#         dan(j)
#         print()
#
# if __name__ == "__main__":
#     gugudan2()
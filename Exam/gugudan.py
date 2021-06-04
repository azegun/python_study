def gugu_dan():
    for i in range(1, 10):
        print()
        for j in range(2, 10):
            print('{} * {} = {:2}'.format(j, i, i * j), end="\t")


gugu_dan()

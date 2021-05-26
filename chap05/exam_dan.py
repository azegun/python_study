def gugudan():
    for i in range(1, 10):
        print()
        for j in range(2, 10):
                print('{} * {} = {:2}'.format(i, j, i * j), end="\t")


if __name__ == "__main__":
    gugudan()

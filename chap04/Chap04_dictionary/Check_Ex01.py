numbers = {1, 1, 2, 3, 4, 5, 1, 2, 3, 3 ,4, 5, 6, 3}
counter = {}

for number in numbers:
    if number in counter:
        counter[number] = counter[number] + 1
    else:
        counter[number] = 1
print(counter)
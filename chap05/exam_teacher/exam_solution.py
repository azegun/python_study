def solution(array, commands):
    answer = []
    # 작업
    for a, b, c in commands:
        answer += [sorted(array[a-1:b])[c-1]]
    return answer

if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    #commands[2]

    result = solution(array, commands)
    print(type(result), result)

# list[5, 6, 3]
def solution2(array, commands):
    return [sorted(array[a-1:b])[c-1] for a, b, c in commands]


if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    #commands[2]

    result = solution2(array, commands)
    print(type(result), result)
dictionary = {}

print("요소 추가 이전: ", dictionary)

dictionary["name"] = "새로운 이름"
dictionary["head"] = "새로운 정신"
dictionary["body"] = "새로운 몸"

print(dictionary)

dictionary1 = {
    "name": "7D 건조 망고",
    "type": "당절임"
}

print("요소 제거 이전", dictionary1)

del dictionary1["name"]
del dictionary1["type"]

print("요소 제거 이후", dictionary1)
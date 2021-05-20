dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

key = input(" > 접근하고자 하는 키 :")

# if key in dictionary:
#     print(dictionary[key])
# else:
#     print("존재하지 않는 키에 접근 하고있습니다.")

value = dictionary.get("존재하지 않는 키")
print("값: ", value)

if value == None:
    print("존재하지 않는 키에 접근했었습니다.")
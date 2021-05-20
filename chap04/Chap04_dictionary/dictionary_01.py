#딕셔너리를 선언합니다.

dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타종아황산타트륨", "치자황색소"],
    "origin": "필리핀"
}

#출력합니다.
# print("name:", dictionary["name"])
# print("type:", dictionary["type"])
# for i in dictionary["ingredient"]:
#     print("ingredient:", i)
# print("origin:", dictionary["origin"])
# print()
#
# #갑을 변경합니다.
# dictionary["name"] = "8D 건조 망고"
# print("name:", dictionary["name"])
#
# dictionary["price"] = 5000
# print(dictionary)
#
# dictionary["name"] = "빠인애쁠"
# print(dictionary)

for key in dictionary:
    print(key, " : ", dictionary[key])
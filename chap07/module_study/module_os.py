import os

print("현재 운영체제 : ", os.name)
print("현재 폴더 : ", os.getcwd())
print("현재 폴더 내부의 요소 : ", os.listdir)

#폴더를 만들고 제거합니다(폴더가 비어있을 떄만 제거 가능).
print(not os.path.exists("hello"))
if not os.path.exists("hello"):
    os.mkdir("hello")

if os.path.exists("hello"):
    os.rmdir("hello")
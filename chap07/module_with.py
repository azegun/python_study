#파일을 생성하고 + 파일 이름을 변경합니다.
import os

with open("original.txt", "w") as file:
    file.write("hello")

os.rename("original.txt", "new.txt")

#파일을 제거합니다
os.remove("new.txt")


std_list = [["1", "김상건", 90, 80, 70],
            ["2", "이나연", 80, 80, 60]]

if not os.path.exists("std_list.txt"):
    # if os.path.isfile("std_list.txt"):
     with open("std_list.txt", "w", encoding="utf-8") as f:
         for std in std_list:
            format_str = "{}, {}, {}, {}, {}\n".format(std[0], std[1], std[2], std[3], std[4])
            print(std)
            f.write(format_str)


std_list2 = []

with open("std_list.txt", "r", encoding="utf-8") as f:
    for line in f:
        std = line.strip().split(",")
        print("std : ", std, type(std))
        std = int(std[0]), std[1], int(std[2]), int(std[3]), int(std[4])
        #투플에서 리스트로 바꿔줄떄는 list()
        std_list2.append(list(std))


print("파일로 읽어 들은 std_List[]", std_list2)

#시스템 명령어 실행
os.system("dir")
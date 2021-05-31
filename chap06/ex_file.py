# try:
#     file = open("into.txt", "w")
#     예외.발생해라()
#
# except Exception as e:
#     print(e)
# finally:
#     file.close()
#
# print("# 파일이 제대로 닫혔는지 확인하기")
# print("file.closed :" , file.closed )

def write_text_file(filename, text):
    try:
        file = open(filename, "w")
        return
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        file.close()

write_text_file("test.txt", "안녕하세요!")
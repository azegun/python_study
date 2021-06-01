import sys

print(sys.argv)
print("-------")

#컴퓨터 환경과 관련된 정보를 출력합니다.
print("getwindowsversion() : ", sys.getwindowsversion())
print("-------")

print("copyright() : ", sys.copyright)
print("--------")

print("version() : ", sys.version)

sys.exit()
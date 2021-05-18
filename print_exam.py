print("#하나만 출력1")
print()

print("#하나만 출력2", "abce", sep="\n", end="\n\n")
print("결과", end="\n\n")

print(type('하나만'), type("하나만"), type(12), type(12.5), sep="\n", end="\n\n")

print("안녕하세요" * 3)

print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])

print()

print("안녕하세요"[-1])
print("안녕하세요"[-2])
print("안녕하세요"[-3])
print("안녕하세요"[-4])
print("안녕하세요"[-5])

print()

print("안녕하세요"[1:4], end='\n')
print("안녕하세요"[:3], end='\n')
print("안녕하세요"[3:], end="\n")

hello = "안녕하세요"
print(type(hello), hello[0:2], hello, sep='\n', end='\n\n')

print(len("안녕하세요"))
print()

# res = input("답정너~~~~~~~")
# print("입력한 답은 " + res)



a = "10 11 a b 14".split(" ")
print(type(a), a,  sep="\n")

x, y, z = 10, 20, 30
print(x, y, z, sep='\n', end='\n')

x, y = y,x
print(x, y, sep='\n', end='\n')
import test_module as test

#최상위는 main이라는 네임을 가짐.
#Module은 main이 아님.
#if조건문으로 조건 주면 됨
if __name__ == "__main__":
    radius = test.number_input()
    print(test.get_circumference(radius))
    print(test.get_circle_area(radius))
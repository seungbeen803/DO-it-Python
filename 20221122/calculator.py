# 클래스(설계도) 쓰는 방법
# 1. Class를 입력하고
# 2. 대문자로 시작하는 클래스의 이름을 작성
# 3. 안에 들어갈 함수와 변수 설정
class Calculator:
    # pass -> 아무것도 안하는 것
    # -__init__ : 처음 클래스가 만들어질 때 어떤 값을 설정할지 설정해주는 것
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
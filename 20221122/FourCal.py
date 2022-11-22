class FourCal:
    # 클래스변수 : 클래스에 미리 선언해둔 변수

    # self : 클래스 안에 있는 함수, 찍어낸 객체
    # a -> self
    # 실행하면서 시작하는 것이 __init__이다
    # __init__ : 선언할 때 무조건 맨 처음 실행됨
    # _init__ : 생성자 한 번만 작성하는 것이 좋다
    def __init__(self, first, second): # 객체변수
        self.first = first
        self.second = second
        
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

# 괄호 안에 부모의 클래스를 넣어 상속 받은 자식 클래스 생성
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
# 자식에게도 __init__함수가 동일하게 동작함
a = MoreFourCal(4, 2)
b = SafeFourCal(5,2)
print(a.add())
print(a.pow())
print(a.mul())
print(a.sub())
print(a.div())
print(b.div())
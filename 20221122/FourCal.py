class FourCal:
    # self : 클래스 안에 있는 함수, 찍어낸 객체
    # a -> self
    # 실행하면서 시작하는 것이 __init__이다
    # __init__ : 선언할 때 무조건 맨 처음 실행됨
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

# 괄호 안에 부모의 클래스를 넣어 상속 받은 자식 클래스 생성
class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4, 2)
print(a.add())
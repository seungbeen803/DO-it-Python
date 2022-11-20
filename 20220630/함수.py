# 함수
# 과일(입력) -> 믹서기(함수) -> 과일주스(출력)

# add함수 - 일반함수
import re


def add(a, b):
    return a + b;
print(add(3, 5))

def add(a, b):
    result = a + b;
    return result;
print(add(3, 4))

# 입력값이 없는 함수
def say():
    return 'Hi';
print(say())

def add(a, b):
    print("{0}, {1}의 합은 {2}입니다.".format(a, b, a+b))
add(3, 7)
add(6, 8)

a = add(3, 4) # 결괏값은 오직 return 명령어로만 돌려받을 수 있다.
print(a)

# 입력값도 결괏값도 없는 함수
def say():
    print('Hi')
say()

# 매개변수 지정하여 호출하기
def add(a, b):
    return a+b
    
result = add(a=3, b=7)
print(result)

# 여러 개의 입력값을 받는 함수 만들기
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result
print(add_many(1, 2, 3))


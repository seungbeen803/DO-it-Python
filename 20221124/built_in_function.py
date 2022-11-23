# 내장함수

# abs => 절댓값
print(abs(-3))
print(abs(3))

# all =>모두 참인지 검사
print(all([1, 2, 3]))
print(all([1,2, 3, 0]))

# any => 하나라도 참이 있는가?
print(any([1, 2, 3, 0]))
print(any([0, ""]))

# chr => ASCII 코드를 입력받아 문자 출력
# ASCII(아스키 코드) = 0~127사이의 숫자를 각 문자에 대응
print(chr(97))
print(chr(48))

# divmod => 몫과 나머지를 튜플 형태로 돌려줌
print(divmod(7, 3))
print(divmod(1.3, 0.2))

# enumerate => 열거하다
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# eval => 실행 후 결과값을 돌려줌
print(eval('1+2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))

# filter => 함수를 통과하여 참인 것만 돌려줌
def positive(x):
    return x > 0
a = list(filter(positive, [1, -3, 2, 0, -5, 6]))
print(a)

a = list(filter(lambda x : x>0, [1, -3, 2, 0, -5, 6]))
print(a)

# id => 주소 값
a = 3
print(id(3))
print(id(a))

b = a
print(id(b))

# list => 리스트로 변환
print(list("python"))
print(list((1, 2, 3)))

a = [1, 2, 3]
b = list(a)
print(b)

# map => 각 요소가 수행한 결과를 돌려줌
def two_times(x):
    return x*2
a = list(map(two_times, [1, 2, 3, 4]))
print(a)

a = list(map(lambda a: a*2, [1, 2, 3, 4]))
print(a)
# 문자열 포매팅(Formatting)
# format() 함수 사용
print("현재 온도는 {}도입니다.".format(18))

# 1. 숫자 바로 대입
print("I eat %d apples." %3) # I eat 3 apples.

# 2. 문자열 바로 대입
print("I eat %s apples." % "five") # I eat five apples.

# 3. 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." % number) # I eat 3 apples.

# 4. 2개 이상의 값 넣기
number = 3
day = "three"
print("I eat %d apples. so I was sick for %s days." %(number, day)) # I eat 3 apples. so I was sick for three days.
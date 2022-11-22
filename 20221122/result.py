result = 0
def add(num):
    # 전역변수에 영향을 주려면 global을 적어야한다
    global result
    result += num
    return result

print(add(3))
print(add(4))

# 클래스를 만드는 이유 : 반복되는 변수 & 메서드(함수)를
# 미리 정해놓은 틀(설계도)
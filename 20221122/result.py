result = 0
def add(num):
    # 전역변수에 영향을 주려면 global을 적어야한다
    global result
    result += num
    return result

print(add(3))
print(add(4))
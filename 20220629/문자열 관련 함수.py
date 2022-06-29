# 문자 개수 세기(count)
a = "hobby";
print(a.count('b')) # 2

# 위치 알려주기(find)
a = "Python is the best choice"
print(a.find('b')) # 14
print(a.find('k')) # -1 -> 값이 존재하지 않는다면 -1이 출력된다.

# 위치 알려주기(index)
a = "Life is too short"
print(a.index('t')) # 8

# 문자열 삽입(join)
print(", ".join('abcd'))
print(" ".join('apples'))

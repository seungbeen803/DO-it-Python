# 입력받은 데이터 합 구하기
li = []
in_list = input("데이터 입력 : ")
li.append(in_list)

def func_sum(in_list):
    sum = 0
    li = in_list.split(" ")
    for i in range(len(li)):
        sum += int(li[i])
    return sum
print("합 : ", func_sum(in_list))
# str 함수 정의
def star(shape, *args):
    for i in range(len(args)):
        print(shape * args[i])
star("♬", 3)

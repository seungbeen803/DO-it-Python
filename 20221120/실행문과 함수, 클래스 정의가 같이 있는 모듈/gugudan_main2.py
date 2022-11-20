# gugudan2_main.py
import gugudan2
def main():
    for i in range(9, 10):
        print("="*20)
    gugudan2.gugudan(i)
# 메인 모듈로 실행될 경우 __name__ 내장 변수가 __main__으로 설정되는 것을
# 이용하여 메인 모듈로 실행된 경우에만 gugudan(3) 함수가 호출되도록 하고 있다.
if __name__ == "__main__":
    main()
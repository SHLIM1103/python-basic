a = input()
b = input()
print(a + b)  # input 은 String 으로 처리한다 !
print(a - b)  # String 이므로 마이너스 연산은 Error 이지만, 파이썬은 인터프리터 언어이므로 실행했을 때에만 연산이 틀렸는지 알 수 있다 !

a = int(input())  # String -> int 로 변환하는 것
b = int(input())
print(a + b)

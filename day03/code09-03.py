""" 변수의 유효범위 우선순위 :: 지역(우선) > 전역 """
def func1():
    global a  # 글로벌: 지역변수를 전역변수화
    a = 10  # 지역변수 -> 3번라인 때문에 전역변수로 오버라이딩
    # global a = 10  # 오류 -> 잘못된 표현 :: 선언 및 초기화는 동시에 하지 않는다
    print("func1에서 a는 %d" % a)

def func2():
    # a = 20  # 지역변수
    print("func1에서 a는 %d" % a)

# 프로그램 출발점
a = 30  # 전역변수

func1()
func2()

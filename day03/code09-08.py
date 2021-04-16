""" 매개변수의 개수를 정하지 않고 전달 :: 파라미터에 튜플을 담는다 """
# 파이썬의 가변매개변수 방식: '*' + 파라미터명 -> 튜플

def plus(*a):  # *변수명 == 튜플(읽기전용 리스트)
    result = 0
    # for i in range(0, len(a)):
    #     result += a[i]
    for i in a:
        result += i
    return result

print(plus(10, 20))
print(plus(10, 20, 30))
print(plus(10, 20, 30, 40, 50))

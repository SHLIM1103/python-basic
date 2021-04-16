""" 매개변수의 기본값을 이용해 오버로딩 역할 대체 """
def plus(v1, v2=0, v3=0):
    return v1 + v2 + v3

# print(plus(10, 20, 30, 40)) # 에러
print(plus(10, 20, 30))
print(plus(10, 20))
print(plus(10))
# print(plus())  # 에러 -> v1 이 없으므로

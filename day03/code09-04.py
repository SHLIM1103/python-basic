""" 반환값이 여러개인 함수 :: 리스트를 반환 """
def multi(v1, v2):
    a = [v1 + v2, v1 - v2]
    return a

print(multi(10, 20))

b = multi(10, 20)
print(b)
print(type(b))

""" 함수의 매개변수 전달 """
def func1(v1, v2):
    return v1 + v2

# def func1(v1, v2, v3):  # Python 은 오버로딩 불가
def func2(v1, v2, v3):
    return v1 + v2 + v3

print(func1(10, 20))
print(func2(10, 20, 30))

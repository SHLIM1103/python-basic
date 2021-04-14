month = int(input("월 입력 : "))

# if-elif 이용
print("if-elif 를 이용한 날짜 찾기")
if month == 1:
    print(31)
elif month == 2:
    print("28 or 29")
elif month == 3:
    print(31)
elif month == 4:
    print(30)
elif month == 5:
    print(31)
elif month == 6:
    print(30)
elif month == 7:
    print(31)
elif month == 8:
    print(31)
elif month == 9:
    print(30)
elif month == 10:
    print(31)
elif month == 11:
    print(30)
elif month == 12:
    print(31)
else:
    print("유효한 월을 입력하세요 !")
print()

# 리스트 이용
print("리스트를 이용한 날짜 찾기")
if month in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif month == 2:
    print(28)
else:
    print(30)
print()

# 딕셔너리 이용
print("딕셔너리를 이용한 날짜 찾기")
def switch(i):  # 딕셔너리를 이용해 switch 를 흉내낼 수도 있다
    return {1: 31, 2: 28, 3: 31}.get(i, -1)  # 키 값에 해당하는 것이 없으면 -1 예외처리
print(switch(month))

import random

# 확률을 각각 다르게 하는 경우 아래와 같음
a = random.randrange(1, 101)
if a == 100:  # 1/100 확률
    print("조커")
elif a >= 90:  # 1/10 확률
    print("백도")
else:
    a %= 5  # 나머지는 0 ~ 4 중 하나
#     if a == 0:
#         print("도")
#     elif a == 1:
#         print("개")
#     elif a == 2:
#         print("걸")
#     elif a == 3:
#         print("윷")
#     else:
#         print("모")

# 리스트를 활용하면 아래와 같음
r = ["도", "개", "걸", "윷", "모"]
print(r[a])

# 모든 확률이 동일한 경우 아래와 같음
# a = random.randrange(1, 8)
# def switch(i):
#     return {1: "도", 2: "개", 3: "걸", 4: "윷", 5: "모", 6: "백도", 7: "조커"}.get(i, -1)
# print(switch(a))

import random

a = random.randrange(1, 7)  # 끝값은 (원하는수 + 1) 로 적용
b = random.randrange(1, 7)

print("a 주사위의 숫자는 %d 입니다" % a)
print("b 주사위의 숫자는 %d 입니다" % b)

if a > b:
    print("a 주사위가 이겼습니다 !")
elif a < b:
    print("b 주사위가 이겼습니다 !")
else:
    print("비겼습니다 !")

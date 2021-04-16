import random

r = random.randrange(1, 101)
print("1 ~ 100 사이의 정수를 맞춰보세요: ", end="")
score = 100

while True:
    i = int(input())
    if score > 0:
        if r == i:
            print("정답! %d 점입니다!" % score)
            break
        elif r < i:
            print("down !  ", end="")
            score -= 10
        else:
            print("up !  ", end="")
            score -= 10
    else:
        print("Game Over !!!")
        break

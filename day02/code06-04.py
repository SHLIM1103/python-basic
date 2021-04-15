# 1 ~ 10 까지의 합을 구하는 for loop
hap = 0
for i in range(1, 11, 1):
    hap += i
print("for loop 합계는", hap)

# 1 ~ 10 까지의 합을 구하는 while loop
hap = 0
i = 1  # while 은 시작값 선언 및 초기화 필수
while i <= 10:
    hap += i
    i = i + 1  # while 은 loop 탈출 조건 필수
print("while loop 합계는", hap)

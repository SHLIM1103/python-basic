for i in range(3, 101, 3):
    print(i, end=" ")
print()

# 1 부터 100 까지 3의 배수 합 구하기
hap = 0
for i in range(3, 101, 3):
    hap += i
print(hap)

# 1 부터 100 까지 3의 배수를 제외한 수의 합 구하기
hap = 0
for i in range(1, 101, 1):
    if i % 3 == 0:
        continue  # 가장 인접한 루프를 탈출하여 위로 진행
    hap += i
print(hap)

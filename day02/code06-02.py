hap = 0  # 변수를 사용할 때에는 반드시 초기값 선언!! 생략시 우변에서 에러
for i in range(1, 10000001, 1):
    hap += i
    # hap = hap + i
print(hap, end=" ")

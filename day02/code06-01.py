for i in range(0, 10, 1):  # 0 ~ 9 범위에서 1씩 증가
    print(i, end=" ")  # 줄바꿈 없이 연속으로 출력
print()

for i in range(0, 10):  # 증가값 1 은 생략 가능
    print(i, end=" ")
print()

for i in range(10):  # 시작값 0 은 생략 가능
    print(i, end=" ")
print()

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:  # range 자리에 리스트도 가능 (불규칙 패턴일 때 유용)
    print(i, end=" ")
print()

for i in range(0, 10, 2):  # 짝수만 출력
    print(i, end=" ")
print()

for i in range(1, 10, 2):  # 홀수만 출력
    print(i, end=" ")
print()

for i in range(10, 0, -1):  # 10 ~ 1 까지 카운트다운 (끝값은 진행방향으로 1 오버해서 설정)
    print(i, end=" ")
print()

for _ in range(1, 5, 1):  # 블럭내 카운터 변수가 필요하지 않을 때에는 언더바(_)로 대체
    print("hi !", end=" ")
print()

for i in range(2, -2, -1):
    print(i, end=" ")
print()

for i in [1, 3, 8]:
    print(i, end=" ")
print()

for i in range(-1, 3):
    print(i, end=" ")

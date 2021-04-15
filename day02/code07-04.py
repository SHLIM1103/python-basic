""" a1 에 한 행씩 리스트를 생성하여, a2 로 한 행씩 통째로 복사하는 다중리스트 """
a1 = []  # 한행용 리스트
a2 = []  # 최종목표인 다중(이차원)리스트
v = 1

""" 다중리스트 생성 """
for i in range(0, 3):  # 총 3행
    for j in range(0, 4):  # 총 4열
        a1.append(v)
        v += 1
    # print(a1)
    a2.append(a1)  # 배열에 배열을 넣은 것
    # print(a2)
    a1 = []

""" 다중리스트 출력 """
for i in range(0, 3):
    for j in range(0, 4):
        print("%3d" % a2[i][j], end=" ")
        # print(a2[i][j], end="\t")  # 위와 같이 정렬시킬 수 있음
    print()

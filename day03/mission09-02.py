import random

# 중복 수를 제외하지 않는 경우
for i in range(1, 7):
    r = random.randrange(1, 46)
    print(r, end=" ")
print()

# 중복 수를 제외하는 경우
numList = []
while len(numList) < 6:  # 리스트 길이를 6개로 맞추기
    r = random.randrange(1, 46)
    if numList.count(r) == 0:  # r이 중복이 아니라면,
        numList.append(r)  # 리스트에 추가하기
        numList.sort()
print(numList)
print()

# 지난주 당첨번호와 일치할 때까지 loop 순환, 로또 구매 금액 구하기
numList = []  # 번호를 채워넣을 리스트
winList = [2, 9, 10, 16, 35, 37]  # 지난주 당첨번호 리스트
money = 0  # 투기 금액

def lotto():
    while len(numList) < 6:  # 리스트 길이를 6개로 맞추기
        r = random.randrange(1, 46)  # 1 ~ 45 까지의 랜덤 수를 뽑기
        if numList.count(r) == 0:  # r이 중복이 아니라면,
            numList.append(r)  # 리스트에 추가하기
    numList.sort()  # 오름차순 정렬

while numList != winList:  # 꽝이면,
    numList.clear()  # 배열을 초기화하고
    lotto()  # 리스트를 채울 loop 다시 돌리기
    money += 1000  # 투기금액 1,000원씩 증가
    # print(numList, "%d원" % money)
    for i in numList:  # 출력 형식 설정
        print("%2d" % i, end=" ")
    print("\t\t", format(money, ","), "원")  # 금액 형식 설정
print("대박이야!!!")  # 당첨 완료

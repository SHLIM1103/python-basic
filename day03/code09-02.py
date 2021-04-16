""" 1부터 사용자가 입력한 정수까지의 합을 반환하는 함수 만들기 """
def hap_to(num):
    hap = 0
    for i in range(1, num + 1):
        hap += i
    return hap

while True:
    a = int(input("1부터 더할 값을 입력(단, 종료는 0 입력): "))
    if a == 0:
        break
    print(hap_to(a))

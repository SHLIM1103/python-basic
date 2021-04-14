i = int(input("동전으로 바꾸기 원하는 금액을 입력하세요 : "))

a = 500
b = 100
c = 10

print("%d원 동전은 %d 개" % (a, i // a))
print("%d원 동전은 %d 개" % (b, i % a // b))
print("%d원 동전은 %d 개" % (c, i % b // c))

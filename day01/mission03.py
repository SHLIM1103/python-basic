a = int(input("숫자1 입력 : "))
b = int(input("숫자2 입력 : "))
print("123456789012345678901234567890")

print("%5d %5s %5d %1s %10d" % (a, "+", b, "=", a + b))
print("%5d %5s %5d %1s %10d" % (a, "-", b, "=", a - b))
print("%5d %5s %5d %1s %10d" % (a, "*", b, "=", a * b))
print("%5d %5s %5d %1s %10d" % (a, "^", b, "=", a ** b))
print("%5d %5s %5d %1s %10.2f" % (a, "/", b, "=", a / b))
print("%5d %5s %5d %1s %10d" % (a, "//", b, "=", a // b))
print("%5d %5s %5d %1s %10d" % (a, "%", b, "=", a % b))

s = input("문자열을 입력하세요: ")

""" 공백의 개수 """
print(s.count(" "))

""" 공백을 제외한 문자열 """
print(s.replace(" ", ""))

""" 숫자를 제거한 문자열 """
ss = ""
for i in range(0, len(s)):
    if not s[i].isdigit():
        ss += s[i]
print(ss)

""" 다른 방법 """
sss = ""
for i in s:
    if not i.isdigit():
        sss += i
print(sss)

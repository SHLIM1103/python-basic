aa = [10, 20, 30, 40, 50]
print(aa[0])  # 결과: 10
print(aa[1:3])  # 결과: [20, 30]
print(aa[3:])  # 결과: [40, 50]
aa.reverse() ; print(aa)  # 결과: [50, 40, 30, 20, 10]

""" 문자열 처리 """
ss = "파이썬최고"
print(ss[0])  # 결과: 파
print(ss[1:3])  # 결과: 이썬
print(ss[3:])  # 결과: 최고

dd = "파이썬" + "만세"
print(dd)  # 결과: 파이썬만세
dd = "파이썬" * 3
print(dd)  # 결과: 파이썬파이썬파이썬

ff = "파이썬abcd"
print(len(ff))  # 결과: 7
print(ff[::-1])  # 결과: dcba썬이파
# ff.reverse()  # 에러 -> 문자열은 reverse() 메소드 불가

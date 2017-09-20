"""
자료형의 참과 거짓
집합, 리스트, 튜플, 딕셔너리에 값이 없으면 false를 반환한다.
"""

a = [1, 2, 3, 4]
while a:
    print(a.pop())

if []: # 안에 아무것도 없으므로 False가 나온다.
    print("True")
else:
    print("False")

if [1, 2, 3]:
    print("True")
else:
    print("False")


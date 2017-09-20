"""
객체
파이썬에서는 자료형을 넣지 않아도 알아서 판단한다.
"""
import sys

a = 1
b = "Python"
c = [1, 2, 3]

# 참조 개수 알아보기 (sys.getrefcount)
print(sys.getrefcount(3)) # 50, 같은 변수를 만들 수록 하나씩 늘어난다.

# 변수를 만드는 여러가지 방법

a, b = ('python', 'life') # 튜플로 a, b에 값을 대입할 수 있다.
(a, b) = 'python', 'life' # 위와 같음.

[a, b] = ['python', 'life'] # 리스트로 변수를 만들 수도 있다.

a = b = 'python'

a = 3
b = 5
a, b = b, a # 두 변수를 간단히 바꿀수도 있다.



# 객체 삭제 (del)
del(a)
del(b)
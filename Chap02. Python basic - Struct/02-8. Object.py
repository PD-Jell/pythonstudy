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

# 리스트를 변수에 넣고 복사할 때
a = [1, 2, 3]
b = a
a[1] = 4
print(a)
print(b)

b = a[:] # :를 이용해서 리스트 전체를 가리킬 수 있다.
a[1] = 4
print(a)
print(b)

from copy import copy
b = copy(a) # copy 명령어를 사용해서 복사할 수 있다.

print(b is a) # is 명령어를 사용해서 같은 객체인지 확인할 수 있다.
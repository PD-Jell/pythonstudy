"""
Set
파이썬 2.3에서부터 지원되기 시작한 자료형.
집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형.

특징
1. 중복을 허용하지 않는다.
2. 순서가 없다(Unordered).
"""

s1 = set([1,2,3])
print(s1) # {1, 2, 3}

s2 = set("Hello")
print(s2) # {'e', 'H', 'l', o'}, 중복되는 건 지우고 알파벳 순으로 나열한다.

# set을 list로 바꾸기
print(list(s1)) # [1, 2, 3]

# set을 tuple로 바꾸기
print(tuple(s1)) # (1, 2, 3)

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1 & s2) # {4, 5, 6}
print(s1.intersection(s2)) # {4, 5, 6}, 같은 함수.

# 합집합
print(s1 | s2) # {1, 2, 3, 4 ,5, 6, 7, 8, 9}
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}, 같은 함수.

# 차집합
print(s1 - s2) # {1, 2, 3}
print(s1.difference(s2)) # {1, 2, 3}, 같은 함수.

# 값 1개 추가하기 (add)
s1.add(4)
print(s1) # {1, 2, 3, 4}

# 값 여러개 추가하기 (update)
s1.update([4, 5, 6])
print(s1) # {1, 2, 3, 4, 5, 6}

# 특정 값 제거하기 (remove)
s1.remove(2)
print(s1) # {1, 3, 4, 5, 6}
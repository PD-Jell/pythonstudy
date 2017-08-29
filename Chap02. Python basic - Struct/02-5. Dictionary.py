"""
Dictionary
딕셔너리는 {와 }로 만든다.
"""

dic = {'name': 'pey', 'phone': '0109993323', 'birth': '1118'}

print(dic)

a = {1: 'hi'} # key는 숫자도 가능.
a = {'a': [1, 2, 3]} # value는 list도 가능.

# 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
print(a) # {1: 'a', 2: 'b'}

a['name'] = 'pey'
print(a) # {1: 'a', 2: 'b', 'name': 'pey'}

a[3] = [1, 2, 3]
print(a) # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 딕셔너리 요소 삭제하기
del a[1]
print(a) # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

grade = {'pey': 10, 'julliet': 99}
print(grade['pey']) # 10
print(grade['julliet']) # 99

a = {1: 'a', 1: 'b'}
print(a) # 'b'
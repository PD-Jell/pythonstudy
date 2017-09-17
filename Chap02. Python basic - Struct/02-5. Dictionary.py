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
print(a) # 'b' or 'a', 어떤 것이 삭제 될 지는 예측할 수 없다. 또한, Key에 리스트를 쓸 수는 없다.

# 딕셔너리 관련 함수들
# Key 리스트 만들기 (keys)
a = {'name': 'pey', 'phone': '0109993323', 'birth': '1118'}
print(a.keys()) # dict_keys(['name', 'phone', 'birth']), 3.0때 추가된 자료형(메모리 낭비를 방지하기 위해)
print(list(a.keys())) # 이렇게 하면 리스트 자료형으로 불러올 수 있음.

# Value 리스트 만들기 (values)
print(a.values()) # 이건 key와 반대로 values를 뽑는 코드.
print(list(a.values())) # 위와 같이 리스트 자료형으로 변환.

# Key-Value쌍 얻기 (items)
print(a.items()) #Key-Value 모두 반환.

# Key-Value쌍 모두 지우기 (clear)
#a.clear()
#print(a) # 모두 지워진다.

# Key로 Value 얻기 (get)
print(a.get('name'))
print(a.get('phone'))

print(a.get('foo', 'bar')) # 값이 없을때에는 미리 정해둔 value를 반환한다.

# 해당 Key가 딕셔너리 안에 있는 지 조사하기 (in)
print('name' in a) # True. 키가 있으면 참, 없으면 거짓을 반환한다.
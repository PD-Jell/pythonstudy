# 문자열 자료형
a = "Life is too short, You need Python"
b = "a"
c = "123"

# 문자열을 만드는 네 가지 방법
# 1. 큰따옴표로 양 쪽 둘러싸기
"Hello world"
# 2. 작은따옴표로 양 쪽 둘러싸기
'Python is fun'
# 3. 큰따옴표 3개를 연속으로 써서 양 쪽 둘러싸기
"""Life is too short, You need python"""
# 4. 작은따옴표 3개를 연속으로 써서 양 쪽 둘러싸기
'''Life is too short, You need python'''

# 문자열 안에 따옴표를 넣고 싶을 때
# 1. 문자열에 작은따옴표 포함시키기
food = "Python's favorite food is perl"
print(food)

# 2. 문자열에 큰 따옴표 포함시키기
say = '"Python is very easy." he says.'

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
# 1. \n넣기
multiline = "Life is too short\nYou need Python."
print(multiline)
# 2. 따옴표 세 개 넣기 (작은 따옴표도 됨!)
multiline = """
Life is too short
You need Python.
"""
print(multiline)

# 문자열 곱하기 응용
a = 'a래여'
print(a * 2) # a래여a래여
print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 인덱싱
a = 'Life is too short, You need Python'
print(a[0]) # L
print(a[12]) # s
print(a[-1]) # n, 마지막 글자

print(a[0:4]) # Life

print(a[5:]) # is too short, You need Python 끝만 지정하는 것도 됨.

a = "Pithon"
a = a[:1] + 'y' + a[2:]

# 문자열 포매팅
print("I eat %d apples." % 3) # 숫자 바로 대입

print("I eat %s apples." % "five") # 문자열 바로 대입

number = 3
print("I eat %d apples." % number) # 변수로 대입

number = 10
day = "Three"
print("I ate %d apples. so I was sick for %s days." % (number, day)) # 2개 이상의 값 넣기.

print("Error is %d%%." % 98) # % 표시할 때는 두번인 거 알지?

# 포맷 코드와 숫자 함께 사용하기
# 1.정렬과 공백
print("%10s" % "hi") # 오른쪽 공백

print("%-10sjane." % 'hi') # 왼쪽 공백

# 2.소수점 표현하기
print("%0.4f" % 3.42134234) # 4번째 소수점까지 표현하기

print("%10.4f" % 3.42134234) # 전체 길이가 10이면서 4번째 소수점까지 표현하기

# 문자 개수 세기(count)
a = "hobby"
print(a.count('b')) # 'b'의 개수를 표시한다. 여기에서는 2.

# 위치 알려주기(find)
a = "Python is best choice"
print(a.find('b')) # b의 index값. 여기에서는 10.
print(a.find('k')) # k의 index값. 여기에서는 없으므로 -1.

# 위치 알려주기2(index)
a = "Life is too short"
print(a.index('t')) # t의 index값. 여기에서는 8.
#print(a.index('k')) # k의 index값. 없으면 오류를 내는 것이 find와 다른 점.

# 문자열 삽입(join)
a = ","
print(a.join("abcd")) # 인자값에 해당 변수를 넣어줌

# 소문자를 대문자로 바꾸기 (upper)
a = "hi"
print(a.upper()) # HI

# 대문자를 소문자로 바꾸기 (lower)
a = "HI"
print(a.lower()) # hi

# 왼쪽 공백 지우기
a = " hi "
print(a.lstrip()) # "hi "

# 오른쪽 공백 지우기
a = " hi "
print(a.rstrip()) # " hi"

# 양쪽 공백 지우기
a = " hi "
print(a.strip()) # "hi"

# 문자열 바꾸기 (replace)
a = "Life is too short"
print(a.replace("Life", "Your leg")) # Your leg is too short

# 문자열 나누기 (split)
a = "Life is too short"
print(a.split()) # "Life" "is" "too" "short"

a = "a:b:c:d"
print(a.split(':')) # "a" "b" "c" "d"

# 고급 문자열 포매팅
# 숫자 바로 대입하기
print("I eat {0} apples".format(3)) # I eat 3 apples

# 문자열 바로 대입하기
print("I eat {0} apples".format("five")) # I eat five apples

# 숫자 값을 가진 변수로 대입하기
number = 3
print("I eat {0} apples".format(number)) # I eat 3 apples

# 2개 이상의 값 넣기

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day)) # I ate 10 apples. so I was sick for three days.

# 인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3)) # I ate 10 apples. so I was sick for 3 days.

# 왼쪽 정렬
print("{0:<10}".format("hi")) # 'hi        ', 앞으로 총 길이가 10임

# 오른쪽 정렬
print("{0:>10}".format("hi")) # '        hi'

# 가운데 정렬
print("{0:^10}".format("hi")) # '    hi    '

# 공백 채우기
print("{0:=^10}".format("hi")) # '====hi===='
print("{0:!<10}".format("hi")) # 'hi!!!!!!!!'

# 소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y)) # '3.4213'
print("{0:10.4f}".format(y)) # '    3.4213'

# '{' 또는 '}' 문자 표현하기
print("{{ and }}".format()) # '{ and }'

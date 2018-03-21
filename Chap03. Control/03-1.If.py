"""
If문을 사용하면 상황에 맞게 프로그램을 제어할 수 있다.
"""

money = 1
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
# money가 1이다. 1은 참이기 때문에, 택시를 타고 가라가 찍히게 된다.

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라") # 2000은 3000보다 작기 때문에 else에 걸린다.

card = 1
if money >= 3000 or card:
    print("택시를 타고 가라") # card가 1이기 때문에 참으로 걸린다.
else:
    print("걸어 가라")

print(1 in [1, 2, 3]) # 1은 [1, 2, 3]에 있기 때문에 참으로 찍힌다.
print(1 not in [1, 2, 3]) # 1은 [1, 2, 3]에 없지 않기 때문에 거짓이 찍힌다.

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass # pass는 C-Style의 continue와 같다.
else:
    print("카드를 꺼내라")

pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라") # elif는 C-Style의 else if와 같다.
else:
    print("걸어가라")

# if문을 한 줄로 작성하기

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass # 바로 이어서 써도 된다.
else: print("카드를 꺼내라")

# 조건부 표현식

score = 71
if score >= 60:
    print("success")
else:
    print("failure")

print("success" if score >= 50 else "failure") # 위의 조건식은 본 줄과 같이 바꿔 쓸 수 있다.

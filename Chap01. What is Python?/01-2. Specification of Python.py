if 4 in [1, 2, 3, 4]: # 행렬은 []로.
    print("4가 있습니다.") # 4가 있으면 출력.

# simple.py
languages = ['python', 'perl', 'c', 'java']

for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")
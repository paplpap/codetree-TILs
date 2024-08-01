a = input()

def aa(a):
    b = len(a)//2 if len(a) % 2 else len(a)//2 + 1
    for i in range(b):
        if a[i] != a[-i-1]:
            print('No')
            exit(0)
    print('Yes')
        


aa(a)
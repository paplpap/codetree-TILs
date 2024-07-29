n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

carry = []

#자릿수 별로 더하기
def lenght(a,b,c):
    flag = True
    for _ in range(n):
        a,a_ = divmod(a,10)
        b,b_ = divmod(b,10)
        c,c_ = divmod(c,10)

        if a_ + b_ + c_ > 10:
            flag = False
            break
    
    return flag


for i in range(n):
    for j in range(i,n-1):
        for k in range(j,n-2):
            a = arr[i]
            b = arr[j]
            c = arr[k]
            if lenght(a,b,c):
                carry.append(a+b+c)

print(max(carry))
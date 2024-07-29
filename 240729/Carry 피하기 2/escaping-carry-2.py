n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

carry = []

#자릿수 별로 더하기
def lenght(a,b,c):
    flag = True
    
    for _ in range(len(str(max(a,b,c)))):
        a,a_ = divmod(a,10)
        b,b_ = divmod(b,10)
        c,c_ = divmod(c,10)

        if (a_ + b_ + c_) >= 10:
            flag = False
            break

    return flag


for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            a = arr[i]
            b = arr[j]
            c = arr[k]
            if lenght(a,b,c):
                carry.append(a+b+c)


if carry == []:
    print(-1)
else:
    print(max(carry))
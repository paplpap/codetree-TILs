n = int(input())
arr = list(map(int,input().split()))

result = [0]*n
for i in range(n):
    for j in range(n):
        if i == j:
            continue

        a = i-j
        if i-j < 0:
            a = -a
        result[i] += arr[j] * a
        
print(min(result))
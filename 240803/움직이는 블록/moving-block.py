n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

cnt = 0
aa = int(sum(arr)/n)
for j in arr:
    if j < aa:
        cnt += aa - j

print(cnt)
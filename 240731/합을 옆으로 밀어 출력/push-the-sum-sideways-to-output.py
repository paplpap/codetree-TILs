n = int(input())

cnt = 0
for i in range(n):
    cnt += int(input())

cnt = str(cnt)

print(cnt[1:]+cnt[0])
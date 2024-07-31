a,b = map(int,input().split())

cnt = []
while True:
    a,n = divmod(a,b)
    

    cnt.append(n)
    if a <= 1:
        break
    

from collections import Counter

count = Counter(cnt)
result = sum(frequency ** 2 for frequency in count.values())

print(result)
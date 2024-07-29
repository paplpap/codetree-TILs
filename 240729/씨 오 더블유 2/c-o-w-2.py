a = int(input())
b = list(input())

cnt = 0
for i in range(a):
    if b[i] == 'C':
        for j in range(i,a):
            if b[j] == 'O':
                for k in range(j,a):
                    if b[k] == 'W':
                        cnt += 1

print(cnt)
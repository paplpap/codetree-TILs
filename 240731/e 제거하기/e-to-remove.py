a = input()

for i in range(len(a)):
    if a[i] =='e':
        a = a[:i] + a[i+1:]
        break

print(a)
n = int(input())

a = ''
while n > 0:
    n,b = divmod(n,2)
    a += str(b)

print(a[::-1])
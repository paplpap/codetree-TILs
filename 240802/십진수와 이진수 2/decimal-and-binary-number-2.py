n = int(input(),2)
n *= 17

a = ''
while n > 0:
    n,b = divmod(n,2)
    a += str(b)

print(a[::-1])
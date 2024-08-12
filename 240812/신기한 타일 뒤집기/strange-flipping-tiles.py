n = int(input())

black = 0
white = 0

now = 'a'

for i in range(n):
    a, b = input().split()
    a = int(a)

    if now == b:
        if b == 'R':
            black -= 1
        else:
            white -= 1


    if now == a:
        if b == 'R':
            black -= 1
        else:
            white -= 1

    if b == 'R':
        black += a
        white -= a


    if b == 'R':
        black += a
        white -= a

    if b == 'L':
        black -= a
        white += a


    if black < 0:
        black = 0

    if white < 0:
        white = 0

    now = b

print(white,black)
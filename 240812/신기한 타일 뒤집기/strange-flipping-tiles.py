n = int(input())

black = 0
white = 0

now = ''

for i in range(n):
    a, b = input().split()
    a = int(a)

    if b == 'R':
        black += a
        white -= a

    if b == 'L':
        black -= a
        white += a

    #print('b:',b,'now:',now)
    #print(white,black)
    if now == b:
        if b == 'R':
            black -= 1
            white += 1
        if b == 'L':
            white -= 1
            black += 1

    if black < 0:
        black = 0

    if white < 0:
        white = 0

    
    now = b


print(white,black)
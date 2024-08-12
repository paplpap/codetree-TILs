n = int(input())

black = 0
white = 0

for i in range(n):
    a, b = input().split()
    a = int(a)

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

print(white,black)
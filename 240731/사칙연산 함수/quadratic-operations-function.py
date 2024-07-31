n = input()
a,o,c = n.split()

a = int(a)
c = int(c)
if o == '+':
    print(n,'=',a+c)
elif o == '-':
    print(n,'=',a-c)
elif o == '*':
    print(n,'=',a*c)
elif o == '/':
    print(n,'=',a/c)
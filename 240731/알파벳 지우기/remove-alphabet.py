a = input()
b = input()

a_num = ''
b_num = ''

for i in a:
    j = ord(i)
    if  47<j<58:
        a_num += i

for i in b:
    j = ord(i)
    if  47<int(j)<58:
        b_num += i

print(int(a_num)+int(b_num))
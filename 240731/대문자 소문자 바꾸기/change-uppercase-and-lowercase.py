a = input()

result = ''
for i in a:
    if i.isupper() == True:
        
        result += i.lower()
    else:
        result += i.upper()
        
print(result)
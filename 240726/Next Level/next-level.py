a,b = input().split()

class game:
    def __init__(self,a='codetree',b=10):
        self.a = a
        self.b = b

qqq = game()
qwe = game(a,b)
print(f'user {qqq.a} lv {qqq.b}')
print(f'user {qwe.a} lv {qwe.b}')
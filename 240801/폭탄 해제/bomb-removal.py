class codeclass:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

        print('code :',code)
        print('color :',color)
        print('second :',second)


code, color, second = input().split()

codeclass(code, color, second)
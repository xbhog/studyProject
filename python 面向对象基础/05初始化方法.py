class TheQueen:
    def __init__(self):
        print('这是一个初始化方法')
        self.name = '小李子'
    def eat(self):
        print('%s吃的贼拉香' %self.name)

cixi = TheQueen()
cixi.eat()

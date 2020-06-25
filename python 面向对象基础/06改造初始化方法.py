class TheQueen:
    def __init__(self,new_name):
        print('这是一个初始化方法')
        self.name = new_name
    def eat(self):
        print('%s吃的贼拉香' %self.name)

cixi = TheQueen('三')
cixi.eat()

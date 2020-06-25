class DelDemo:
    def __init__(self, name):
        self.name = name
        print('-----%s start live----' % self.name)

    def __del__(self):
        print('-----kill  %s live------' %self.name)

    def __str__(self):
        return '----%s隐藏-----' %self.name

helloDel = DelDemo('小强')
print(helloDel)
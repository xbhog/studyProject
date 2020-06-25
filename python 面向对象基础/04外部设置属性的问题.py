class Cat:
    def eat(self):
        print('%s 爱吃李子'  %self.name)

    def drink(self):
        print('%s 的诞辰' %self.name)

# 创建对象
tom = Cat()


tom.eat()
# print(tom)
#增加属性名---修改的位置
tom.name = '小李子'

lazy_cat = Cat()
#lazy_cat增加属性名
lazy_cat.name = '慈溪'

lazy_cat.eat()
lazy_cat.drink()



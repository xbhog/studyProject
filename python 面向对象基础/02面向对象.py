class Cat:
    def eat(self):
        print('小猫吃鱼')

    def drink(self):
        print('小猫爱喝水')

# 创建对象
tom = Cat()
tom.drink()
print(tom)

lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)
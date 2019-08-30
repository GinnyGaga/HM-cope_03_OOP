class Cat:

    def eat(self):
        print(" %s 爱吃鱼" % self.name)

    def drink(self):
        print(" %s 爱喝水" % self.name)

# 创建猫对象
tom = Cat()
# 增加属性
tom.name = "Tom"
# 对象调用方法
tom.eat()
tom.drink()
print(tom)

print("*" * 50)
lazy_cat = Cat()
lazy_cat.name = "大蓝猫"
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

lazy_cat2 = lazy_cat
print(lazy_cat2)

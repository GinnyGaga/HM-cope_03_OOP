class Cat:
    # 在Cat类中封装2个方法

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")

# 创建猫对象
tom = Cat()
# 对象调用方法
tom.eat()
tom.drink()
print(tom)

lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

lazy_cat2 = lazy_cat
print(lazy_cat2)

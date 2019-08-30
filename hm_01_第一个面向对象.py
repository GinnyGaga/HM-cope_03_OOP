# 大驼峰命名法命名类
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

addr = id(tom)
# %d 为10进制度，%x 为16进制
print("%d" % addr)
print("%x" % addr)


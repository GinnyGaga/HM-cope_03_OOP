class Cat:

    def eat(self):
        print(" %s 爱吃鱼" % self.name)

    def drink(self):
        print(" %s 爱喝水" % self.name)

# 创建猫对象
tom = Cat()
# 增加属性
# tom.name = "Tom"
# 对象调用方法
tom.eat()
tom.drink()
tom.name = "Tom"
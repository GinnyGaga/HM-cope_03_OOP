class Cat:
    def __init__(self,new_name):
        print("这是一个初始化方法")
        # self.属性名 = 属性的初始值
        # self.name = "Tom"
        self.name = new_name
    def eat(self):
        print("%s 爱吃鱼" % self.name)

tom = Cat("Tom")
# print(tom.name)
tom.eat()

lazy_cat = Cat("Susan")
lazy_cat.eat()

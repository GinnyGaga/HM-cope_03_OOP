class Woman:
    def __init__(self,name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s 的年龄是 %d " % (self.name,self.__age))

ginny = Woman("金妮")
# 私有属性在外界不能被访问

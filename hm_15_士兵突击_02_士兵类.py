class Gun:
    def __init__(self,model):
        # 1、枪的型号
        self.model = model
        # 2、子弹的数量
        self.bullet_count  = 0

    def add_bullet(self,count):
        self.bullet_count += count
        print("%s 装上了 %d 颗子弹" % (self.model,self.bullet_count))

    def shoot(self):
        # 1、判断是否有子弹
        if self.bullet_count <= 0:
            print("这枪没有子弹")
            return
        # 2、每发射一枪，子弹少一颗
        self.bullet_count -= 1
        # 3、发射后，还剩余的子弹数
        print("子弹还剩余 %d 颗" % self.bullet_count)


class Soldier:
    def __init__(self,name):
        self.name = name
        # 1、新兵没有枪
        self.gun = None

# 1、创建枪对象
model = Gun("AK47")
model.add_bullet(50)
model.shoot()
# 2、创建许三多
xushanduo = Soldier("许三多")
xushanduo.gun = model
print(xushanduo.gun)






class Gun:
    def __init__(self,model):
        # 1、枪的型号
        self.model = model
        # 2、子弹的数量
        self.bullet_count  = 0

    def __str__(self):
        return "这把枪的型号是 %s " % self.model

    def add_bullet(self,count):
        self.bullet_count += count
        print("这把枪装上了 %d 颗子弹" % self.bullet_count)

    def shoot(self):
        # 1、判断是否有子弹
        if self.bullet_count <= 0:
            print("这枪没有子弹")
            return
        # 2、每发射一枪，子弹少一颗
        self.bullet_count -= 1
        # 3、发射后，还剩余的子弹数
        print("子弹还剩余 %d 颗" % self.bullet_count)


model = Gun("AK47")
print(model)
model.add_bullet(50)
model.shoot()
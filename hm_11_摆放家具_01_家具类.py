# 创建家具类
class HouseItem:

    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return "家具名字是 %s，家具占地面积是 %.2f平米。" % (self.name,self.area)

bed = HouseItem("席梦思",3.89)
chest = HouseItem("衣柜",4)
table = HouseItem("餐桌",2)
print(bed)
print(chest)
print(table)


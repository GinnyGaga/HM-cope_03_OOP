class HouseItem:

    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return "家具名字是 [%s]，其占地面积是 %.2f平米。" % (self.name,self.area)

class House:

    def __init__(self,house_type,area):
       self.house_type = house_type
       self.area = area
       self.free_area = area
       self.item_list = []

    def __str__(self):
        return ("房子的户型是: %s \n总面积是 %.2f平米 "
                "[剩余面积是 %.2f平米] \n家具列表是 %s" % (self.house_type,self.area,
                                          self.free_area,self.item_list))

    def add_item(self,item):
        print("要添加 %s " % item)
        # 1、判断家具的面积
        if  item.area > self.free_area:
            print("%s 的面积超过了剩余面积，不能添加！" % item.name)
            return
        # 2、将家具的名称添加到列表中
        self.item_list.append(item.name)
        # 3、计算剩余面积
        self.free_area -= item.area

# 1、创建家具对象
bed = HouseItem("席梦思",10)
chest = HouseItem("衣柜",4)
table = HouseItem("餐桌",200)

print(bed)
print(chest)
print(table)
# 2、创建房子对象
my_home = House("三室一厅",130)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)
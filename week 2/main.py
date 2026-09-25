from pet_vet import Dog,Cat,Vet


dog=Dog(name="旺财",age="3",breed="金毛")
cat=Cat(name="咪咪",age="2",color="白色")

vet=Vet(name="张医生",hospital="爱心宠物医院")

print("===== 宠物自我介绍 =====")
dog.introduce()  # 狗自我介绍
cat.introduce()  # 猫自我介绍

print("\n===== 宠物行为展示 =====")
dog.eat()       # 狗吃饭
dog.sit()       # 狗坐下
dog.roll_over() # 狗打滚
cat.eat()       # 猫吃饭
cat.climb_tree() # 猫爬树
cat.catch_mouse() # 猫抓老鼠

print("\n===== 兽医服务 =====")
vet.examine(dog)   # 兽医检查狗
vet.vaccinate(dog) # 兽医给狗接种疫苗
vet.examine(cat)   # 兽医检查猫
vet.vaccinate(cat) # 兽医给猫接种疫苗
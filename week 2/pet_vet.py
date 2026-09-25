class Pet:
    def __init__(self,name,age,species):
        self.name=name
        self.age=age
        self.species=species

    def introduce(self):
        print(f"我是{self.name},{self.age}岁，是一只{self.species}。")

    def eat(self):
        print(f"{self.name}正在吃饭")


class Dog(Pet):
    def __init__(self,name,age,breed):
        super().__init__(name,age,species="狗")
        self.breed=breed

    def sit(self):
        print(f"{self.name}坐下了")

    def roll_over(self):
          print(f"{self.name}打滚啦！")


class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age,species="猫")
        self.color=color

    def climb_tree(self):
        print(f"{self.name}爬上树了")

    def catch_mouse(self):
        print(f"{self.name}抓到了一只老鼠！")



class Vet:
    def __init__(self,name,hospital):
        self.name=name
        self.hospital=hospital

    def examine(self,Pet):
        print(f"{self.name}医生正在为{Pet.name}检查身体")

    def vaccinate(self,Pet):
        print(f"{self.name}医生为{Pet.name}接种疫苗")
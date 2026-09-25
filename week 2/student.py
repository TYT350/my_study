class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def get_grade(self):
        if self.score>=90:
            return "A"
        elif self.score>=80:
            return "B"
        elif self.score>=60:
            return "C"
        else:
            return "D"


if __name__=="__main__":
    s1=Student("张三",88)
    print(f"学生：{s1.name},分数：{s1.score}，等级：{s1.get_grade()}")
    s2=Student("李四",55)
    print(f"学生：{s2.name},分数：{s2.score}，等级：{s2.get_grade()}")
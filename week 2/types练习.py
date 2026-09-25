print("---数值互转---")
print (int(3.9))
print(float(5))
print(int("123"))
print(float("3.14"))
# 下面这几行会报错，取消注释逐个体验：
# print(int("3.5"))     # ValueError！带小数点的字符串要先 float() 再 int()
# print(int("abc"))     # ValueError！非数字字符串无法转
print("----str->容器（按字符拆分）----")
s="hello"
print(list(s))
print(tuple(s))
print(set(s))#自动去重，且无序


print("----list/tuple/set互转----")
lst=[1,2,2,3,4,5,6]
print(tuple(lst))
print(set(lst))
print(list(set(lst)))


print("----dict互转（重点：默认只拿key）----")
d={"a":1,"b":2}
print(list(d))
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))


#==================== 二、5 种容器操作 ====================
#每种容器练：增、删、改、查（索引/切

#1. list 列表：有序、可变、可重复
print("------1.list--------")
fruits=["苹果","梨子","西瓜"]
fruits.append("橙子")
fruits.insert(0,"草莓")
del fruits[2]
n=fruits.pop()
fruits[1]="葡萄"
fruits.remove("草莓")
print(fruits)
print(fruits,n)
print(fruits[0:1])
print(len(fruits),"苹果" in fruits)


#2. tuple 元组：有序、不可变、可重复
print("------2.tuple------")
not_tuple=(1)
is_tuple=(2,)
print(type(not_tuple),type(is_tuple))

point=(3,4)
x,y=point
print(x,y)
print(point[0],point[-1])
print(point.count(3),point.index(4))


#3. set 集合：无序、可变、不可重复
print("-----3.set-----")
a={1,2,3,4}
b={4,5,6,7}
a.add(99)
a.discard(1)
print(a|b)   #并集
print(a&b)   #交集
print(a-b)   #差集
print(2 in a)


#4. dict 字典：无序、可变、键唯一
print("-----4.dict----")
student={"name":"小米","age":"20"}
student["score"]=90
student["age"]=21
print(student["name"])
print(student.get("gender"))
print(student.get("gender","未填写"))
student.pop("score")
print(student)
print(student.keys(),student.values(),student.items())
      





#5. str 字符串：有序、不可变、可重复
print("-----5.str----")
m="python-test"
print(s[1],s[-1])
print(s[0:7])
print(s.upper())
print(s.replace("-","_"))
print(s.split("-"))
print("-".join (["a","b","c"]))
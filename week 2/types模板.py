# types.py —— Day 9：数据类型互转 + 5 种容器操作
# 运行方式：终端执行 python types.py，对照注释理解每一行输出

# ==================== 一、7 种类型互转 ====================
# 转换函数：int() / float() / str() / list() / tuple() / set() / dict()

print("---- 数值互转 ----")
print(int(3.9))         # 3    float -> int：直接截断小数（不是四舍五入！）
print(float(5))         # 5.0  int -> float
print(int("123"))       # 123  str -> int：字符串必须是纯整数
print(float("3.14"))    # 3.14 str -> float

# 下面这几行会报错，取消注释逐个体验：
# print(int("3.5"))     # ValueError！带小数点的字符串要先 float() 再 int()
# print(int("abc"))     # ValueError！非数字字符串无法转

print("---- str -> 容器（按字符拆分）----")
s = "hello"
print(list(s))          # ['h', 'e', 'l', 'l', 'o']
print(tuple(s))         # ('h', 'e', 'l', 'l', 'o')
print(set(s))           # {'h', 'e', 'l', 'o'}  自动去重，且无序

print("---- list / tuple / set 互转 ----")
lst = [1, 2, 2, 3, 3, 3]
print(set(lst))         # {1, 2, 3}      list -> set：最常用的一行去重
print(list(set(lst)))   # [1, 2, 3]      去重后转回 list
print(tuple(lst))       # (1, 2, 2, 3, 3, 3)  list -> tuple：生成不可变快照

print("---- dict 互转（重点：默认只拿 key）----")
d = {"a": 1, "b": 2}
print(list(d))            # ['a', 'b']            只拿到 key！
print(list(d.keys()))     # ['a', 'b']            显式拿 key
print(list(d.values()))   # [1, 2]                拿 value
print(list(d.items()))    # [('a', 1), ('b', 2)]  拿键值对（二元组列表）

pairs = [("a", 1), ("b", 2)]      # 反向：键值对序列 -> dict
print(dict(pairs))        # {'a': 1, 'b': 2}

# ==================== 二、5 种容器操作 ====================
# 每种容器练：增、删、改、查（索引/切片）+ 特有操作

# 1. list 列表：有序、可变、可重复
print("\n---- 1. list ----")
fruits = ["苹果", "香蕉", "橙子"]
fruits.append("葡萄")           # 增：尾部追加
fruits.insert(0, "西瓜")        # 增：指定位置插入
fruits[1] = "草莓"              # 改：按索引赋值
fruits.remove("橙子")           # 删：按值删除
last = fruits.pop()             # 删：弹出末尾元素并返回它
print(fruits, "| pop 弹出:", last)
print(fruits[0], fruits[-1])    # 查：正索引 / 负索引（-1 是最后一个）
print(fruits[1:3])              # 查：切片（含头不含尾）
print(len(fruits), "草莓" in fruits)  # 长度 + 成员判断

# 2. tuple 元组：有序、不可变、可重复
print("\n---- 2. tuple ----")
not_tuple = (1)                 # 这是 int！括号只是运算符
is_tuple = (1,)                 # 单元素元组必须带逗号
print(type(not_tuple), type(is_tuple))

point = (3, 5)
x, y = point                    # 解包：一次给多个变量赋值
print(x, y)
print(point[0], point[-1])      # 查：只能读，不能增删改
# point[0] = 9                  # 取消注释会报 TypeError：元组不可修改
print(point.count(3), point.index(5))  # 统计出现次数 / 查位置

# 3. dict 字典：键值对、可变、key 不可重复
print("\n---- 3. dict ----")
student = {"name": "小明", "age": 20}
student["score"] = 90           # 增：key 不存在就是新增
student["age"] = 21             # 改：key 存在就是覆盖
print(student["name"])          # 查：[] 取值，key 不存在会报 KeyError
print(student.get("phone"))     # 查：get() 取不到返回 None，不报错（更安全）
print(student.get("phone", "未填写"))  # get 还能指定默认值
student.pop("score")            # 删：按 key 删除
print(student)
print(student.keys(), student.values(), student.items())  # 三大视图

# 4. set 集合：无序、不重复、可变
print("\n---- 4. set ----")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a.add(99)                       # 增
a.discard(1)                    # 删：元素不存在也不报错（remove 会报 KeyError）
print(a)
print(a | b)                    # 并集：两边所有的
print(a & b)                    # 交集：共有的
print(a - b)                    # 差集：a 有 b 没有
print(2 in a)                   # 成员判断（set 比 list 快得多）

# 5. str 字符串：有序、不可变的字符序列
print("\n---- 5. str ----")
s = "python-test"
print(s[0], s[-1])              # 查：索引
print(s[0:6])                   # 查：切片 -> python
print(s.upper())                # 返回新串，原串不变
print(s.replace("-", "_"))      # 替换：python_test
print(s.split("-"))             # 拆成 list：['python', 'test']
print("-".join(["a", "b", "c"]))  # list 拼回 str：a-b-c
# s[0] = "P"                    # 取消注释会报 TypeError：字符串不可修改

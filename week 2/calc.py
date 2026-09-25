def add(a,b):
    """加法"""
    return a+b

def sub(a=0,b=0):
    """减法"""
    return a-b

def mul(a,b):
    """乘法"""
    return a*b

def div(a,b):
    """除法"""
    if b==0:
        return "除数不能为0"
    return a/b
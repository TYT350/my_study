#1. 数字是 3 的倍数 → 输出 `Fizz`
#2. 数字是 5 的倍数 → 输出 `Buzz`
#3. 同时是 3 和 5 倍数 → 输出 `FizzBuzz`
#4. 其他情况，直接输出数字
lst=range(1,101)
for i in lst:
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

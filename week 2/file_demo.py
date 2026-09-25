def file_operate():
    file_name="test.txt"
    try:
        with open (file_name,"r",encoding="utf-8") as f:
            content=f.read()
            print("读取到的内容：")
            print(content)

    except FileNotFoundError:
    
        print(f"警告：文件{file_name}不存在")
        with open (file_name,"w",encoding="utf-8")as f:
            f.write("这是新写入的测试文本\nHello Python 文件读写")
        print("写入完成！")
if __name__=="_main_":
    file_operate()
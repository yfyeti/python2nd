from random import randint

# 生成一个随机数
guessnum = randint(1, 100)


def getnum():
    gn = input("请输入一个整数：")
    while not gn.isdigit():
        gn = input("输入内容必须为整数：")
    return int(gn)


# 用户输入整数
num = getnum()
# 比较随机数大小，并输出提示
while num != guessnum:
    if num > guessnum:
        print("大大大大了,",end="")
        num = getnum()
    else:
        print("这么小小小啊,",end="")
        num = getnum()
else:
    # 猜对输出结果
    print("很不幸！你猜对了")

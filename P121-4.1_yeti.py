from random import randint
# 生成一个随机数
guessnum = randint(1, 9)
# 用户输入整数
try:
    num = eval(input("请输入一个整数："))
except NameError:
    print("Error")
# 比较随机数大小，并输出提示
while num != guessnum:
    if num > guessnum:
        num = int(input("大了大了，往小死精猜！！！"))
    else:
        num = int(input("小了小了，怎么这么小！！！"))
else:
    # 猜对输出结果
    print("很不幸！你猜对了")

restperiod = input("请输入多少天休息一天：")
upup = 1  # 能力值
restday = 0  # 休息日
for i in range(1, 366):
    if i % (eval(restperiod) + 1) != 0:  # 判断是否是休息日
        if (365 - restday + (i - 1) % 7) % 7 in [4, 5, 6, 0]:
            upup *= (1 + 0.01)
            print("今天提升日，我提升了%f" % upup)
        else:
            w123d = ((365 - restday + (i - 1) % 7) % 7)
            print("今天是工作的第%d天" % w123d)
            continue
    else:
        restday = i
        print("今天是第%d天，今天休息" % i)
        continue
print("最终那能力提升%f" % upup)

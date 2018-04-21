···
炉石传说龙牧，带了dragon张龙牌，前4回合抽到aoe的概率
···

from random import *

while 1:
    dragon = eval(input("请输入龙的数量"))
    str1 = "d" * dragon + "n" * (28 - dragon) + "a" * 2
    lst1 = list(str1)
    dd = 0
    pd = 0
    sdd = 0
    times = 10000
    for t in range(times):
        shuffle(lst1)
        drcount = 0
        for i in range(1, 11):
            draoe = choice(lst1)
            if draoe == "d" or draoe == "a":
                drcount += 1
                # print("我在第{}张牌抽到了龙牌".format(i))
            if draoe == "a":
                if drcount > 2:
                    dd += 1
                    pd = dd / i
                    break

    print("{}次中前4回合内抽到AOE的次数是{}".format(times, dd))
    print("在前4张抽到AOE的概率是{:.2%}".format(dd / times))

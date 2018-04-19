while 1:
    from random import *
    fcho=0
    scho=0
    a=int(input("请输入2以上的整数表示羊的个数："))
    time=100000
    for i in range(time):
        result=randint(0,a)
        if result==0:
            fcho+=1
        elif randint(0,a-2)==0:
            scho+=1
    print("不改变选择获得车的概率为：{:.3f}".format(fcho/time))
    print("改变选择获得车的概率为：{:.3f}".format(scho/time))

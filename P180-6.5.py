from random import randint

prsnum = eval(input("请输入房间人数："))
times = 100000
percent = 0
for t in range(times):
    person = []
    for pn in range(prsnum):
        person.append(randint(1, 366))
    for pn in person:
        if person.count(pn) >= 2:
            percent += 1
            break

print("概率为{:.2%}".format(percent/times))

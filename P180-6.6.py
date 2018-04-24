import jieba
txt = open('红楼梦.txt', "r", encoding="gb18030").read()
words = jieba.lcut(txt)
counts = {}

excludes = {"什么", "一个", "我们", "你们", "如今", "说道", "知道", "姑娘", "起来", "这里", "出来", "众人",
            "那里", "自己", "太太", "一面", "只见", "两个", "没有", "怎么", "不是", "不知", "这个", "听见",
            "这样", "进来", "奶奶", "咱们", "就是", "东西", "告诉", "回来", "只是", "大家", "老爷", "只得",
            "丫头", "这些", "他们", "不敢", "出去", "所以", "不过", "不好", "姐姐", "的话", "一时", "鸳鸯",
            "过来", "不能", "心里", "他们", "如此", "银子", "她们", "今日", "二人", "答应", "这么", "几个",
            "还有", "只管", "说话", "那边", "一回", "这话", "外头"}


for word in words:
    if len(word) == 1:
        continue
    elif word == "贾母" or word == "老太太":
        rword = "贾母"
    elif word == "凤姐" or word == "王夫人" or word == "凤姐儿":
        rword = "凤姐"
    elif word == "贾琏" or word == "二爷":
        rword = "贾琏"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1

for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(12):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))

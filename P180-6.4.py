this="""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
this=this.replace(chr(32),"")
this=this.replace(chr(10),"")
this=this.lower()
dict1={}
for c in this:
    dict1[c]=dict1.get(c,0)+1

list1=list(dict1.items())
list1.sort(key=lambda x:x[1],reverse=True)
print("总计使用字符{}个".format(len(list1)))
for i in range(12):
    word,count=list1[i]
    print("{0:<4}总计使用{1:>5}个 - unicode为{2}".format(word,count,ord(word)))

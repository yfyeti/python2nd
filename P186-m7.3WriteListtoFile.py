fname = input("请输入要写入的文件: ")
fo = open(fname, "w+")
ls = ["唐诗", "宋词", "元曲"]
fo.writelines(ls)
for line in fo:
    print(line)
fo.close()

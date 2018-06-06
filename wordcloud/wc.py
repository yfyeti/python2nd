#做自己的词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
from PIL import Image

# import jieba
# words=''
# with open('红楼梦.txt', "r", encoding="gb18030") as hlm:
#     for line in hlm.readlines():
#         line=line.strip('\n')
#         words+=''.join(jieba.cut(line))
#         words=words.replace('道','')
#         words = words.replace('笑', '')
#         words+=''


#处理自己的数据
filename="arthas.txt"
with open(filename,"r") as f:
    arthastxt=f.read()
bimg=plt.imread("mw.jpg")   #读图片
wordcloud=WordCloud(background_color='white',mask=bimg).generate(arthastxt)


image_colors =ImageColorGenerator(bimg)
wordcloud.recolor(color_func=image_colors)
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
wordcloud.to_file("wc3.png")
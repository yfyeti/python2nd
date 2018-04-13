# RANDOM

## Seed
## Random
### 整数
1.randint(a,b)  
2.getrandbits(k)  
3.randrange(start,stop[,step])

### 小数
1.random()  
2.uniform(a,b)

### 序列
1.choice(seq)  
2.shuffle(seq)  
3.sample(pop,k) 


```
from random import choice

list1 = [3.3, 4.3, 4.6, 4.7]
ch = choice(list1)
if ch == 3.3 or ch == 4.3:
    list1.remove(3.3)
    list1.remove(4.3)
else:
    list1.remove(4.6)
    list1.remove(4.7)
ch2 = choice(list1)
print("您选择的题目是{},{}".format(ch, ch2))
```

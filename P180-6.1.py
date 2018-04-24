from random import sample

lst1 = []
for i in range(49, 58):
    lst1.append(chr(i))
for c in range(97, 123):
    lst1.append(chr(c))
# print(lst1)

for p in range(10):
    print("".join(sample(lst1, 8)))

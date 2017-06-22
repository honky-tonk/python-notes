import random
a = []
for i in range(65,91):
    a.append(i)
b = []
for n in range(97,123):
    b.append(n)
c = []
for m in range(48,58):
    c.append(m)
a.extend(b)
a.extend(c)
d=[]
for i in a:
    d.append(chr(i))
for i in range(10):
    print(random.sample(d,8))
    

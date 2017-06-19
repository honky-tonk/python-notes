import time
print("------执行开始------")
scl = 10
for i in range(scl+1):
    a,b = "**" * i,".." * (scl-i)
    c = i/10*100
    print("%{:3.0f}[{}->{}]".format(c,a,b))
    time.sleep(0.3)
print("------执行结束------")    

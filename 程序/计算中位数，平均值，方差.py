from math import sqrt
def getnum():  #输入总数
    nums = []
    iNumstr = input("请输入数字(输入回车退出):")
    while iNumstr != "":
        nums.append(eval(iNumstr))
        iNumstr = input("请输入数字(输入回车退出):")
    return nums
def avg(number):    #平均数
    s = 0.0
    for num in number:
        s = s + num
    return s / len(number)
def dev(avg,number): #方差
    sdev = 0.0
    for num in number:
        sdev = sdev + (num-avg)**2
    return sqrt(sdev / len(number))
def median(number):  #中位数
    sorted(number)
    a = len(number)
    if a / 2 == 0:
        return (number[a // 2] + number[a // 2 - 1]) / 2
    else:
        return number[a // 2]







number = getnum()  #总的数组
avg = avg(number)  #平均值
dev = dev(avg,number)  #方差
median = median(number)  #中位数

print("平均值是:{}，方差是:{}，中位数是:{}".format(avg,dev,median))
    

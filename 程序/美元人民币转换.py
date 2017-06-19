money = input("请输入金额数量:")
if money[-1] in ["$"]:
    c = (eval(money[0:-1])*6)
    print("转换后的温度是:{}￥".format(c))
elif money[-1] in ["￥"]:
    c = (eval(money[0:-1])/6)
    print("转换后的结果为:{}$".format(c))
else:
    print("输出错误！")
    

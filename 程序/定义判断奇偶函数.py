
def isOdd(n):
    if n % 2 == 1:
        return("奇数")
    elif n % 2 == 0:
        return("偶数")
while True:
    m = input("请输入整数")
    if isinstance(eval(m),int) == 1:
        print(isOdd(m))
        break
    else:
        print("input error try agint")
    
            


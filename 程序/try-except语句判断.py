'''
try:
    a = eval(input("请输入数字："))   #把需要的语句包含到try-except语句里 输入的结果用eval函数把字符转换成数字如果输入其他字符会报nameerror错误 如果直接输出也会报另一个错误
    num = a * 3    #  输入的结果乘三
    print(num)  #输出这个标识符
except NameError:   #当报错的信息为NameError时就会执行下面的语句如果报其他的错误就不会执行下面的语句
    print("NameError!!!!") #当报错为NameError时执行print函数

except:  #当报其他除NmaeError错误之外的错误输出以下语句
    print("其他错误")
'''


def f1 ():
    f2 ()
def f2 ():
    print("函数f2()")
f1 ()

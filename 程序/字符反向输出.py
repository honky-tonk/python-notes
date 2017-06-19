def fact(n):
    if n == "":
        return ""
    else:
        return fact(n[1:]) + n[0]
print(fact(input("请输入字符")))

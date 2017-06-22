def gettxt():#得到文件所有内容
    txt = open(r"C:\Users\张浩然\Desktop\Hamlet.txt","r",encoding = "utf-8").read()
    txt = txt.lower()
    for char in "~!@#$%^&*(-)?_+{}|:.,'/ ":
        txt = txt.replace(char," ")
    return txt
def tongji():   #统计单词出现数
    a = gettxt()
    words = a.split()
    allsum = {}
    for word in words:
        allsum[word] = allsum.get(word,0) + 1
    return allsum
a = tongji()
b = list(a.items())
b.sort(key=lambda x:x[1],reverse=True)  #sort方法有2个参数一个key一个reverse, key就是list的元素把list的元素交给后面处理这个list每一个元素都是tulple所以区每一个list元素里的第二个元素作为判断大小的标准，reverse参数有两个选项一个True一个False判断它们是否要反序排序也就是从大到小
for i in range(10):
    word,count = b[i]
    print("单词{}出现了{}".format(word,count))

    

def jishuqi(inputlist):
    if isinstance(inputlist,list) == False:
        return print("this is not list")
    else:
        a = {}
        b = 0
        
        for i in inputlist:
            for n in range(len(inputlist)):
                if i == inputlist[n]:
                    b = b+1               
                elif i != inputlist[n] :
                    b = b+0
            a[i]=int(b)
            b = 0
        return a
aa = ["zzz","zzz","xxx","xxx","ccc"]
bb = jishuqi(aa)
print(bb)
'''
for i in bb.keys():
    if i == 1:
        print(aa[i])
    else:
        print("")
'''

from turtle import *
color("red", "yellow")   #选择颜色
begin_fill()
while True:
    forward(200)   #长度
    left(181)    # 旋转460度
    if abs(pos()) < 1:
        break
end_fill()
done()

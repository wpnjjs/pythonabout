# coding:utf-8

'''
@author: monster
@file: aturtle.py
@time: 2017/12/19 上午10:53
'''
'''turtle 海龟 。只听得懂有限的指令。它在一个横轴为x、纵轴为y的坐标系原点，(0,0)位置开始，它根据一组函数指令的控制，在这个平面坐标系
中移动，从而在它爬行的路径上绘制了图形。'''

import turtle

# 设置画布大小和背景

turtle.screensize(400, 300, "green")
turtle.title("welcome to the turtle zoo")
turtle.position()
turtle.forward(15)
turtle.position()

# 特殊的turtle窗口方法，不是继承至TurtleScreen类
# turtle.bye()  # 关闭窗口
turtle.exitonclick()  # 点击关闭窗口

# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 23:45
# @Author  : Nixin
# @Email   : nixin@foxmail.com
# @File    : HelloWorld.py
# @Software: PyCharm

import math

a = eval(input("请输入三角形边长a:"))
b = eval(input("请输入三角形边长b:"))
T = eval(input("请输入三角形两边夹角"))

# 角度转为弧度
t = math.radians(T)
c = math.sqrt(a*a+b*b-2*a*b*math.cos(t))
print("第三边的边长为：{:.2f}".format(c))
input()

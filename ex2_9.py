# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 13:44:11 2018

@author: 李娟
"""
import turtle
turtle.setup(1300,800,0,0)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("blue")
turtle.seth(-40)
for i in range(5):
    turtle.circle(40,80)
    turtle.pencolor("purple")
    turtle.circle(-40,80)
    turtle.pencolor("blue")
    turtle.circle(-40,80)
circle(40,40)
turtle.pencolor("black")
fd(40)
turtle.circle(16,160)
turtle.pensize(36)
fd(40*2/3)

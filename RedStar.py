# -*- coding: utf-8 -*-
'''
Created on Thu Jan  9 14:44:34 2020

@author: Pope  Zheng
'''
import turtle
side = eval(input("Enter the side and see the mystery: \n"))

turtle.showturtle()
turtle.color("red")
turtle.setheading(72)
turtle.forward(side)
turtle.setheading(288)
turtle.forward(side)
turtle.right(144)
turtle.forward(side)
turtle.right(144)
turtle.forward(side)
turtle.right(144)
turtle.forward(side)

turtle.done()

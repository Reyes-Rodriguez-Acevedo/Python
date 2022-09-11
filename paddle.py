# -*- coding: utf-8 -*-
"""
Created 2022-09-02

@author: rrodriguez
"""
from turtle import Turtle

class Paddle(Turtle):
	def __init__(self, x, y):
		super().__init__()
		self.shape("square")
		self.color("white")
		self.shapesize(stretch_len=20 / 20, stretch_wid=100 / 20)
		self.penup()
		self.goto(x, y)


	def go_up(self):
		position_x = self.xcor()
		position_y = self.ycor()
		self.goto(x=position_x, y=position_y + 20)


	def go_down(self):
		position_x = self.xcor()
		position_y = self.ycor()
		self.goto(x=position_x, y=position_y - 20)


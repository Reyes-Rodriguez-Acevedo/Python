# -*- coding: utf-8 -*-
"""
Created 2022-09-02

@author: rrodriguez
"""
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 70, "bold")

class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()
		self.l_score = 0
		self.r_score = 0
		self.update_scoreboard()


	def update_scoreboard(self):
		self.goto(x=-100, y=200)
		self.write(self.l_score, align= ALIGNMENT, font=FONT)
		self.goto(x=100, y=200)
		self.write(self.r_score, align= ALIGNMENT, font=FONT)
		self.goto(x=-100, y=-280)
		self.write(arg="W = Go Up\nZ = Go Down", align= ALIGNMENT, font=("Courier", 14, "bold"))
		self.goto(x=100, y=-280)
		self.write(arg="U = Go Up\nN = Go Down", align= ALIGNMENT, font=("Courier", 14, "bold"))


	def l_point(self):
		self.clear()
		self.l_score += 1
		self.update_scoreboard()


	def r_point(self):
		self.r_score += 1
		self.clear()
		self.update_scoreboard()


	def game_over(self):
		self.goto(x=0, y=0)
		self.write(arg="GAME OVER", align= ALIGNMENT, font=FONT)

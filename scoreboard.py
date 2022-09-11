# -*- coding: utf-8 -*-
"""
Created 2022-09-01

@author: rrodriguez
"""
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.color("white")
		self.penup()
		self.hideturtle()
		self.goto(x=0, y=260)
		self.update_scoreboard()


	def update_scoreboard(self):
		self.write(arg=f"Score: {self.score}", align= ALIGNMENT, font=FONT)


	def increase_score(self):
		self.score += 1
		self.clear()
		self.update_scoreboard()


	def game_over(self):
		self.goto(x=0, y=0)
		self.write(arg="GAME OVER", align= ALIGNMENT, font=FONT)

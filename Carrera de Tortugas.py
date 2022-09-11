# -*- coding: utf-8 -*-
"""
Created 2022-08-30

@author: rrodriguez
"""
# 181. Aaaand, we're off to the races!
from turtle import Turtle, Screen, colormode
import random

screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
screen.bgcolor("black")
screen.title("My Turtle Race")

border = Turtle()
border.pencolor("white")
border.penup()
border.goto(240, -185)
border.pendown()
border.goto(240, 195)
border.goto(-245, 195)
border.goto(-245, -185)
border.goto(240, -185)

text = Turtle()
text.color("white")
text.penup()


def win():
	text.write(f"You won! \n The {winning_color} turtle \n is the winner!", align="center", font=("Courier", 16, "normal"))


def lost():
	text.pendown()
	text.write(f"You lost! \n The {winning_color} turtle \n is the winner!", align="center", font=("Courier", 16, "normal"))


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-160, -96, -32, 32, 96, 160]
all_turtles = []

is_race_on = False


for turtle_index in range(0,6):
	new_turtle = Turtle(shape ="turtle")
	new_turtle.shapesize(4, 4, 4)
	new_turtle.color(colors[turtle_index])
	new_turtle.speed("fastest")
	new_turtle.penup()
	new_turtle.goto(x = -210, y = y_positions[turtle_index])
	all_turtles.append(new_turtle)

user_bet = screen.textinput(title = "Make your bet", prompt = "Which Turtle win the race? Enter a color: ")

if user_bet:
	is_race_on = True

while is_race_on:

	for turtle in all_turtles:
		if turtle.xcor() >= 210:
			is_race_on = False
			winning_color = turtle.pencolor()
			if winning_color == user_bet:
				print(f"You won! The {winning_color} turtle is the winner!")
				win()
			else:
				print(f"You lost! The {winning_color} turtle is the winner!")
				lost()
		rand_distance = random.randint(0, 10)
		turtle.forward(rand_distance)

screen.exitonclick()

# -*- coding: utf-8 -*-
"""
Created 2022-08-31

@author: rrodriguez
"""
import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

border = Turtle()
border.pencolor("white")
border.penup()
border.goto(290, -290)
border.pendown()
border.goto(290, 295)
border.goto(-295, 295)
border.goto(-295, -290)
border.goto(290, -290)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()

screen.onkey(snake.up, key= "Up")
screen.onkey(snake.down, key= "Down")
screen.onkey(snake.left, key= "Left")
screen.onkey(snake.right, key= "Right")


def touch(x,y):
	snake.head.left(90)

screen.onclick(touch)

game_is_on = True

while game_is_on:
	screen.update()
	time.sleep(0.1)

	snake.move()

	# Detect collision with food
	if snake.head.distance(food) < 15:
		# print("nom nom nom")
		food.refresh()
		snake.extend()
		score.increase_score()

	# Detect collision with the wall.
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		score.game_over()
		game_is_on = False

	# Detect collision with the tail.
	# if head collides with any segment in the tail
	# slice despues del primer segmento hasta el final
	for segment in snake.segments[1:]:
		# if segment == snake.head:
		# 	pass
		if snake.head.distance(segment) < 10:
			score.game_over()
			game_is_on = False


# screen.exitonclick()

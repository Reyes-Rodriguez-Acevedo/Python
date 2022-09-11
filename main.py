# -*- coding: utf-8 -*-
"""
Created 2022-09-02

@author: rrodriguez
"""
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

border = Turtle()
border.pencolor("white")
border.penup()
border.goto(390, -290)
border.pendown()
border.goto(390, 295)
border.goto(-395, 295)
border.goto(-395, -290)
border.goto(390, -290)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

ball = Ball()

score = Scoreboard()

screen.listen()

screen.onkey(fun=r_paddle.go_up,key="u")
screen.onkey(fun=r_paddle.go_up,key="U")
screen.onkey(fun=r_paddle.go_down, key="n")
screen.onkey(fun=r_paddle.go_down, key="N")
screen.onkey(fun=l_paddle.go_up,key="w")
screen.onkey(fun=l_paddle.go_up,key="W")
screen.onkey(fun=l_paddle.go_down, key="z")
screen.onkey(fun=l_paddle.go_down, key="Z")

game_is_on = True

while game_is_on:
	screen.update()
	time.sleep(ball.move_speed)
	ball.move()

	# Detecting collision with the wall.
	if ball.ycor() > 280 or ball.ycor() < -280:
		# needs to bounce.
		ball.bounce_y()

	# Detecting collision with paddles.
	if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
		ball.bounce_x()
		ball.move_speed /= 1.25

	# Detecting R paddle missing
	if ball.xcor() > 380:
		ball.reset_position()
		score.l_point()
		if score.l_score >= 5:
			game_is_on = False

	# Detecting L paddle missing
	if ball.xcor() < -380:
		ball.reset_position()
		score.r_point()
		if score.r_score >= 5:
			game_is_on = False


screen.exitonclick()


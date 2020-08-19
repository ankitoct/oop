# Python program to draw
# Spiral Square Outside In and Inside Out
# using Turtle Programming
import turtle #Outside_In
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk = turtle.Turtle()
skk.color("magenta")

def sqrfunc(size):
	for i in range(10):
		skk.fd(size)
		skk.left(45)
		size = size-5

sqrfunc(14)
sqrfunc(12)
sqrfunc(10)
sqrfunc(85)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)

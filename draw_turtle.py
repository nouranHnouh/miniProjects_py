#draw figure using turtle module
import turtle
#def draw_triangle():
	#tom=turtle.Turtle()
	#i=0
	#while i<4:
		#tom.forward(100)
		#tom.left(120)
		#i=i+1


def draw_turtle():
	window=turtle.Screen()
    #background color of the screen
	window.bgcolor("red")
	#creates and returns new turtle object
	brad=turtle.Turtle()
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(1) 
	i=0
	while i<40:
		brad.forward(100)
		brad.right(90)
		brad.right(10)
		i=i+1 

	"""angie=turtle.Turtle()
	angie.color("yellow")
	angie.shape("arrow")
	angie.circle(100)
	"""
	#tria=draw_triangle()

	window.exitonclick()


draw_turtle()

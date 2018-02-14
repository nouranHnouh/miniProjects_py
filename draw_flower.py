import turtle
def draw_triangle(tom):
	i=0
	while i<4:
		tom.forward(100)
		tom.left(120)
		i=i+1
def draw_flower():
	window=turtle.Screen()
	window.bgcolor("red")
	
	tria=turtle.Turtle()
	tria.shape("arrow")
	tria.speed('normal')
	tria.color("black","blue")
	

	#tria.circle(20)
	for i in range (1,27):
		draw_triangle(tria)
		tria.forward(100)
		tria.left(50)
        
		
	
	



draw_flower()
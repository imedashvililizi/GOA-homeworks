from turtle import*
#we want to paint a house

#step1: draw a square
speed(20)
width(7)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square

#drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end of door

penup()
goto(200,200)
pendown()

#drawing a roof
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of roof

penup()
goto(180,180)
pendown()

#drawing a window
color("blue")
begin_fill()
left(30)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)

penup()
goto(20,180)
pendown()

forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()
#end of window


exitonclick()

from turtle import*

#drawing a house

#draw a square
speed(20)
width(5)
color("blue")
forward(180)
left(90)
forward(180)
left(90)
forward(180)
left(90)
forward(180)
left(90)

#drawing a door

forward(70)
color("green")
begin_fill()
left(90)
forward(80)
right(90)
forward(40)
right(90)
forward(80)
end_fill()

#end of door


penup()
goto(180,180)
pendown()

#drawing a roof
color("light blue")
begin_fill()
right(150)
forward(180)
left(120)
forward(180)
end_fill()

penup()
goto(160,160)
pendown()

#begin a window
color("light green")
begin_fill()

right(60)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)

penup()
goto(20,160)
pendown()

left(90)
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
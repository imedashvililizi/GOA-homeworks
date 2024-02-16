from turtle import*
speed(100)
width(4)
color("brown")
begin_fill()
forward(130)
left(90)
forward(150)
left(90)
forward(130)
left(90)
forward(150)
left(90)
end_fill()

#drawing a door

forward(50)
left(90)
color("orange")
begin_fill()
forward(60)
right(90)
forward(30)
right(90)
forward(60)
end_fill()



penup()
goto(110,135)
pendown()

#begin a window
color("grey")
begin_fill()
forward(50)
right(90)
forward(35)
right(90)
forward(50)
right(90)
forward(35)



penup()
goto(20,136)
pendown()

forward(35)
right(90)
forward(50)
right(90)
forward(35)
right(90)
forward(50)
end_fill()


penup()
goto(130,150)
pendown()

 #drawing a roof
    
color("red")
begin_fill()
left(45)
forward(95)
left(90)
forward(95)
end_fill()

#house 2

penup()
goto(0,0)
pendown()

color("blue")
begin_fill()
right(45)
forward(130)
right(90)
forward(150)
right(90)
forward(130)
right(90)
forward(150)
end_fill()
#drawing a door

left(270)


forward(50)
left(270)
color("black")
begin_fill()
forward(50)
left(90)

begin_fill()
forward(30)
left(90)
forward(50)



left(90)
forward(30)
end_fill()

penup()
goto(-20,130)
pendown()
#drawing window
color("green")
begin_fill()
right(90)
forward(40)
right(90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)

penup()
goto(-110,130)
pendown()

forward(30)
right(90)
forward(40)
right(90)
forward(30)
right(90)
forward(40)
end_fill()

penup()
goto(0,150)
pendown()

#drawing a roof
color("purple")
begin_fill()
left(45)
forward(95)
left(90)
forward(95)
end_fill()


#house 3
penup()
goto(-130,0)
pendown()

right(45)
color("light green")
begin_fill()
forward(130)
right(90)
forward(150)
right(90)
forward(130)
right(90)
forward(150)
end_fill()

#begin a door
right(90)

begin_fill()
forward(50)
color("pink")
right(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
end_fill()

penup()
goto(-150,130)
pendown()

#drawing a window
color("purple")
forward(40)

begin_fill()
right(90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)
end_fill()

penup()
goto(-200,130)
pendown()

color("purple")
begin_fill()
right(90)

forward(40)
right(90)
forward(30)
right(90)
forward(40)
right(90)
forward(30)
end_fill()

penup()
goto(-130,150)
pendown()

left(135)
color("yellow")
begin_fill()
forward(95)
left(90)
forward(95)
end_fill()




penup()
goto(-400,-4)
pendown()

color("dark green")
begin_fill()
left(135)
forward(720)
right(90)
forward(100)
right(90)
forward(720)
right(90)
forward(100)
end_fill()


penup()
goto(200,-4)
pendown()

color("brown")
begin_fill()
forward(150)
right(90)
forward(40)
right(90)
forward(150)
right(90)
forward(40)
right(90)
forward(150)
end_fill()

color("light green")
begin_fill()
left(90)
forward(40)
right(90)
forward(100)
right(90)
forward(120)
right(90)
forward(100)
right(90)
forward(40)
end_fill()


penup()
goto(-130,360)
pendown()

color("yellow")
begin_fill()
circle(40)
end_fill()



exitonclick()


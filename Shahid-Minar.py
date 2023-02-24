import turtle

dpen=turtle.Turtle()
dpen.width(3)
dpen.color("white")
new=turtle.getscreen()
dpen.speed(6)

new.bgcolor("black")


#niche neya
dpen.penup()
dpen.left(180)
dpen.forward(350)
dpen.left(90)
dpen.forward(250)


#pillar 1
dpen.pendown()
dpen.right(180)
dpen.forward(180) #u1
dpen.right(90)
dpen.forward(60) #p1
dpen.right(90)
dpen.forward(180) #u2
dpen.right(90)
dpen.forward(10) #p2
dpen.right(90)
dpen.forward(170) #u3
dpen.left(90)
dpen.forward(40) #p3
dpen.left(90)
dpen.forward(170) #u4
dpen.right(90)
dpen.forward(10) #p4

#END OF PILLAR 1
dpen.penup()
#PILLAR 2
dpen.right(180)
dpen.forward(80)
dpen.pendown()
dpen.left(90)
dpen.forward(260) #u1
dpen.right(90)
dpen.forward(60) #p1
dpen.right(90)
dpen.forward(260) #u2
dpen.right(90)
dpen.forward(10) #p2
dpen.right(90)
dpen.forward(250) #u3
dpen.left(90)
dpen.forward(40) #p3
dpen.left(90)
dpen.forward(250) #u3
dpen.right(90)
dpen.forward(10)

#END OF PILLAR 2
dpen.penup()
#pillar 3
dpen.right(180)
dpen.forward(120) 
dpen.pendown()
dpen.left(90)
dpen.forward(290) #u1
dpen.left(15)
dpen.forward(160) #p1
dpen.right(105)
dpen.forward(350) #u2
dpen.right(105)
dpen.forward(160) #p2
dpen.right(-15)
dpen.forward(290) #u3
dpen.right(90)
dpen.forward(20) #p3
dpen.right(90)
dpen.forward(290)
dpen.left(-15)
dpen.forward(150)
dpen.left(105)
dpen.forward(175)
dpen.left(105)
dpen.forward(150)
dpen.left(-15)
dpen.forward(290)
dpen.right(90)
dpen.forward(15)
dpen.right(90)
dpen.forward(290)
dpen.left(15)
dpen.forward(150)
dpen.left(75)
dpen.forward(115)
dpen.left(105)
dpen.forward(150)
dpen.left(-15)
dpen.forward(290)
dpen.right(90)
dpen.forward(20)
 #END OF PILLAR 3

#pillar 4
dpen.right(180)
dpen.penup()
dpen.forward(350)
dpen.left(90)
dpen.pendown()
dpen.forward(260)
dpen.right(90)
dpen.forward(60)
dpen.right(90)
dpen.forward(260)
dpen.right(90)
dpen.forward(10)
dpen.right(90)
dpen.forward(250)
dpen.left(90)
dpen.forward(40)
dpen.left(90)
dpen.forward(250)
dpen.right(90)
dpen.forward(10)
#END OF PILLAR 4
dpen.penup()
#PILLAR 5
dpen.right(180)
dpen.forward(80)
dpen.pendown()
dpen.left(90)
dpen.forward(180) #u1
dpen.right(90)
dpen.forward(60) #p1
dpen.right(90)
dpen.forward(180) #u2
dpen.right(90)
dpen.forward(10) #p2
dpen.right(90)
dpen.forward(170) #u3
dpen.left(90)
dpen.forward(40) #p3
dpen.left(90)
dpen.forward(170) #u4
dpen.right(90)
dpen.forward(10) #p4
#end of pillar 5

dpen.penup()
dpen.right(180)
dpen.forward(60)
dpen.right(90)
dpen.forward(20)
dpen.right(90)
dpen.forward(350)

turtle.done()
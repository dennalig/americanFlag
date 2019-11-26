import turtle
drw = turtle.Turtle()
#turns turtle to face up
drw.left(90)

#Makes center point of star


def toppoint (ang1, ang2, length):
    drw.right(ang1)
    drw.forward(length)
    drw.right(ang2)
    drw.forward(length)
    
toppoint (15,135,5)
#Makes other points

def point(angl, angr, length):

    drw.left(angl)
    drw.forward(length)
    drw.right(angr)
    drw.forward(length)
    
for i in range (4):
     point(60,135,5)

angl = 60
angr = 135
length = 5
     

     

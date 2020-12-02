import turtle # turtle writer 
from matplotlib.colors import is_color_like # https://stackoverflow.com/questions/42876366/check-if-a-string-defines-a-color
# this checks if the user input for the colors are valid 
def checkColorInput(name): # checks if it is a valid color 
    name = name.lower()
    name = name.strip()
    while(not is_color_like(name)):
        name = input("Please enter a valid color: ")
        name = name.lower()
        name = name.strip()
    
    return name #returns color

colorName = input("Enter a preffered Background color: ") 
colorName= checkColorInput(colorName) # background call

#inner rectangle
innerColor = input("Enter a preffered Inner color: ")
innerColor = checkColorInput(innerColor) # stripe call

#first stripe 
stripe1 = input("Enter a preffered stripe (red place) color: ")
stripe1 = checkColorInput(stripe1)

#second stripe 

stripe2 = input("Enter a preffered stripe (white place) color: ")
stripe2 = checkColorInput(stripe2)


drw = turtle.Turtle()
drw.speed(100000000000000000)
drw.dot(2000000, colorName) # preffered color is placed in 
#Moves turtle to top left
drw.penup()
drw.left(90)
drw.forward(300)
drw.left(90)
drw.forward(370)
drw.left(180)






def drawrectangle (distl, disth):
    drw.pendown()
    for i in range(2):
        drw.forward(distl)
        drw.right(90)
        drw.forward(disth)
        drw.right(90)
    drw.penup()
#Draws large rectangle
drawrectangle(700,400)

#Draws small rectangle

drw.color(innerColor,innerColor)
drw.begin_fill()
drawrectangle(315,199.98)
drw.end_fill()


drw.forward(315)
drw.right(90)



def stripe(color, num):
    #color changes between red and white for each stripe 
    #num is the length of the stripe 
        drw.forward(30.769)
        drw.pendown()
        drw.color(color,color)
        for j in range(2):
            drw.begin_fill()
            drw.left(90)
            drw.forward(num)
            drw.left(90)
            drw.forward(30.769)
            drw.end_fill()
            drw.penup()
#Draws first 6 stripes
for k in range(3):
    stripe(stripe1,385)
    stripe(stripe2,385)
drw.color('black')

#positions turtle for next set of stripes
drw.right(90)
drw.forward(315)
drw.left(90)

#Draws last 7 stripes
for l in range(3):
    stripe(stripe1,700)
    stripe(stripe2,700)
stripe(stripe1,700)

#positions turtle for star formation in the top left corner of flag 
drw.color('black','black')
drw.penup()
drw.right(180)
drw.forward(400)

drw.right(90)
drw.forward(10)
drw.left(90)

#makes a star 
def star(dist):
    drw.backward(dist)
    drw.pendown()
    drw.color(stripe2,stripe2) # stripe2 is also the color of the stars 
    drw.begin_fill()
    def toppoint(ang1, angr2, length):
        drw.right(ang1)
        drw.forward(length)
        drw.right(angr2)
        drw.forward(length)
    toppoint (15,135,5)

    #angl= angle left, angr=angle right
    def point(angl, angr, length):
        drw.left(angl)
        drw.forward(length)
        drw.right(angr)
        drw.forward(length)
    for i in range (4):
     point(60,135,5)
    drw.end_fill()
    drw.left(90)
    drw.penup()
    
#makes row of stars
def starrow():
    star(10)
    for m in range(4):
        star(40)
    drw.forward(168)

    
#Makes the outerspread 6 rows     
for n in range(6):
    starrow()
    drw.right(90)
    drw.forward(50)
    drw.left(90)

#positions turtle for second row 
drw.left(90)
drw.forward(294)
drw.right(90)

def starrow2():
    star(30)
    for p in range(3):
        star(40)
    drw.forward(148.5)

for q in range (5):
    starrow2()
    drw.right(90)
    drw.forward(50)
    drw.left(90)

    
drw.forward(50)

turtle.done() # exits on exit







    





#drw.forward(30.769)
#400/ (13 is number of stripes) --> 30.769

#Values
#33.33 is distance between each stripe
#6 is the number of stipes on the first part of flag beside the star box

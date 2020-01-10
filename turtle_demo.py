from turtle import Turtle, Screen

def Water():
    leo.penup()
    leo.setx(-200)
    leo.fillcolor('blue')

    leo.begin_fill()

    for _ in range(2):
        leo.forward(400)
        leo.right(90)
        leo.forward(150)
        leo.right(90)

    leo.end_fill()

    leo.pendown()

def Building():
    leo.fillcolor('darkslategrey')

    for height in bheight:
        leo.begin_fill()
        leo.left(90)
        leo.forward(height)
        leo.right(90)
        leo.forward(20)
        leo.right(90)
        leo.forward(height)
        leo.left(90)
        leo.end_fill()

blist = input('Please enter building heights e.g. "50 30 60": ')
bsplit = blist.split()
bheight = list(map(int, bsplit))

screen = Screen()
screen.bgcolor("orange")

leo = Turtle()

Water()
Building()

screen.mainloop()
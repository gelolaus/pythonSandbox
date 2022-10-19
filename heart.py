# Heart using turtle with message

import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")

# Draw the heart
tess = turtle.Turtle()
tess.color("red")
tess.pensize(3)

tess.left(140)

tess.forward(180)
tess.circle(-90, 200)
tess.setheading(60)
tess.circle(-90, 200)
tess.forward(180)

# Write the message
tess.penup()
tess.setheading(90)
tess.forward(20)
tess.setheading(0)
tess.forward(20)
tess.pendown()
tess.color("black")
style = ('Arial', 30, 'italic')
tess.write('I love you!', font=style, align='center')
tess.hideturtle()

wn.mainloop()
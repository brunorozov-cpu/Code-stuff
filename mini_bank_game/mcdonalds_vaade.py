import turtle
from time import sleep

screen = turtle.Screen()
screen.setup(1100, 750)
screen.bgcolor("#d9d9d9")
screen.title("McDonalds - Sa oled nüüd kassapidaja")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def rect(x, y, w, h, fill, outline="black", pensize=2):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pensize(pensize)
    t.color(outline, fill)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

def polygon(points, fill, outline="black"):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.color(outline, fill)
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])
    t.end_fill()

rect(-550, -50, 1100, 500, "white")
rect(-550, 300, 1100, 70, "#c40000")
rect(-550, 370, 1100, 40, "#eeeeee", outline="#cccccc")

for i in range(3):
    rect(-400 + i*320, 120, 280, 150, "#111111")
    rect(-380 + i*320, 140, 240, 20, "#ffcc00")
    rect(-380 + i*320, 170, 240, 10, "#ff4444")
    rect(-380 + i*320, 190, 200, 8, "#ffaa00")

rect(-180, -20, 360, 150, "#c0c0c0")
rect(-160, 0, 320, 110, "#f5f5f5", outline="#999999")

polygon([(-550,-250),(550,-250),(480,-120),(-480,-120)], "#7a4b2c")
polygon([(-480,-120),(480,-120),(430,-80),(-430,-80)], "#5c3820")

rect(-120, -200, 240, 140, "#444444")
rect(-90, -60, 180, 100, "#000000")
rect(-70, -30, 140, 40, "#00cc66", outline="#003300", pensize=1)
rect(-70, 20, 140, 15, "#cccccc", outline="#666666", pensize=1)
rect(150, -170, 80, 90, "#333333")
rect(165, -120, 50, 30, "#00ccff")

t.penup()
t.goto(-40, 330)
t.pendown()
t.color("#ffcc00")
t.pensize(18)
t.setheading(90)
t.circle(40, 180)
t.penup()
t.goto(40, 330)
t.pendown()
t.setheading(90)
t.circle(40, 180)

screen.update()
sleep(3)


t = turtle.Turtle()
t.hideturtle()
t.speed(0)

screen.addshape("Epstein.gif")
mees = turtle.Turtle()
mees.shape("Epstein.gif")
mees.penup()
mees.goto(-200, -100)

def tee_texti_mull(t, tekst, x, y, font_suurus=14):
    t.penup()
    laius = len(tekst)*11
    kõrgus = font_suurus + 19
    t.goto(x - laius/2, y - kõrgus/2)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(2):
        t.forward(laius)
        t.left(90)
        t.forward(kõrgus)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(x, y - font_suurus/3)
    t.color("black")
    t.write(tekst, align="center", font=("Arial", font_suurus, "normal"))

# Näita teksti mehe kohal
x, y = mees.xcor(), mees.ycor()
sleep(1.75)
tee_texti_mull(t, "Pane mu friikad ilusti kotti ära nüüd!", x, y + 210, font_suurus=19)
screen.addshape("Epstein.gif")

pilt = turtle.Turtle()
pilt.shape("Epstein.gif")
pilt.penup()

pilt.goto(-300, 0)
scale = 1.0
pilt.shapesize(scale, scale)

def paremale():
    pilt.setx(pilt.xcor() + 20)
def vasakule():
    pilt.setx(pilt.xcor() - 1000)
def yles():
    pilt.sety(pilt.ycor() + 20)
def alla():
    pilt.sety(pilt.ycor() - 20)

def suuremaks():
    global scale
    scale += 2
    pilt.shapesize(scale, scale)

def vaiksemaks():
    global scale
    if scale > 1:
        scale -= 1
        pilt.shapesize(scale, scale)


screen.listen()
screen.onkey(paremale, "Right")
screen.onkey(vasakule, "Left")
screen.onkey(yles, "Up")
screen.onkey(alla, "Down")
screen.onkey(suuremaks, "plus")
screen.onkey(vaiksemaks, "minus") 
pilt.stamp()
pilt.hideturtle()

screen.mainloop()
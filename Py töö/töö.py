#from import kaka siin, ALALALALA!
from turtle import *
from random import randint
# Ruut taust
side = 600
penup()
goto(-side/2, -side/2)
pendown()
color("black", "orange")
begin_fill()
for i in range(4):
    forward(side)
    left(90)
end_fill()
penup()
hideturtle()
import turtle
konto_tekst = turtle.Turtle()
konto_tekst.hideturtle()
konto_tekst.penup()

#Konto loomise kiri
def kiri(sõnum, y_offset=0):
    konto_tekst.goto(-side/2 + 20, side/2 - 60 + y_offset)
    konto_tekst.write(sõnum, font=("Courier", 14, "normal"))

# Vale PIN code
teade = Turtle()
teade.hideturtle()
teade.penup()
teade.goto(-side/2 + 20, side/2 - 90)
teade.color("black")

#Konto loomine
kiri("Tere tulemast pangaautomaati!", 30) 
kiri("Loo endale konto!")
nimi = textinput("Nime küsimine", "Palun sisesta om nimi:")
kood1 = textinput("PIN-sisestus", "Loo endale PIN-1:")
kood2 = textinput("PIN-sisestus", "Loo endale PIN-2:")
konto_tekst.clear()

# PIN-kontroll 3 katsega
katseid = 3
while katseid > 0:
    kiri("Logige sisse pangaautomaati!")
    pin1 = textinput("PIN-sisestus", "Palun sisesta PIN-1:")
    pin2 = textinput("PIN-sisestus", "Palun sisesta PIN-2:")
    konto_tekst.clear()
    
    if kood1 == pin1 and kood2 == pin2:
        teade.clear()
        break
    else:
        katseid -= 1
        teade.clear()  # <<<Kustutab eelmise teate
        if katseid > 0:
            teade.write(f"Vale PIN! Jäänud on {katseid} katset.", font=("Courier", 14, "normal"))
        else:
            teade.write("Konto on lukustatud!", font=("Courier", 14, "normal"))
            exitonclick(pin2, pin1)

# Kui PIN õige
konto = 100
kiri("Pangaautomaat", 20)
kiri("Tere! " + nimi +"!", -20)
kiri("Sisenesite kontosse!\n", -80)
kiri("Teie kontol on " + str(konto) + " €.", -100)

soovitud_raha = textinput("Väljavõtt", "Palju soovite välja võtta?")
try:
    soovitud_raha = int(soovitud_raha)
except:
    kiri("Vale sisestus!", -130)
    exitonclick()

if soovitud_raha <= konto:
    konto -= soovitud_raha
    kiri(f"Võtsite {soovitud_raha} € välja!", -160)
    kiri(f"Alles on {konto} €.", -190)
else:
    kiri("Kontol on liiga vähe raha!", -160)
    casino = textinput("Kasiino", "Kas soovite teenida raha juurde? (jah/ei)")
    if casino and casino.lower() == "jah":
        kasutaja_valik = textinput("Kasiino", "Red (1) või Black (2)?")
        konto_tekst.clear()
        try:
            kasutaja_valik = int(kasutaja_valik)
        except:
            kiri("Vale sisestus!", -190)
            exitonclick()
        suvaline_arv = randint(1, 2)
        if kasutaja_valik == suvaline_arv:
            konto += 100
            kiri(f"BIG WIN! Te võitsid Paksu Rihardi ja 100€!", 20)
            kiri(f"Teie kontol on nüüd {konto}€ ja Paks Rihard.", -20)
            screen = getscreen()
            screen.addshape("lel.gif")
            p = Turtle()
            p.shape("lel.gif")
            p.resizemode("user")
            p.shapesize(0.5, 0.5)
            p.penup()
            p.goto(0, 0)
           
        else:
            konto = 0
            kiri("Sa kaotasid kogu oma raha :(", 20)
            screen = getscreen()
            screen.addshape("bob.gif")
            p = Turtle()
            p.shape("bob.gif")
            p.resizemode("user")
            p.shapesize(0.5, 0.5)
            p.penup()
            p.goto(0, 0)
    else:
        kiri("Ole vaene rott edasi siis...", -190)

exitonclick()
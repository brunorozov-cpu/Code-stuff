#from import kaka siin, ALALALALA!
from turtle import *
from random import randint
from tkinter import messagebox
from time import sleep
import sys
import time

#Roulette table
def display_animation_casino():
    tracer(0)
    laud = Turtle()
    laud.hideturtle()
    laud.speed(0)
    nool = Turtle()
    nool.hideturtle()
    nool.speed(0)
    nool.color("white")
    nool.width(4)
    sektorid = 12
    raadius = 120
    nurk = 360 / sektorid
    värvid = ["red", "black"] * (sektorid // 2)

    def joonista_rulet(pööre):
        laud.clear()

        for i in range(sektorid):
            laud.penup()
            laud.goto(0, 0)
            laud.setheading(pööre + i * nurk)
            laud.fillcolor(värvid[i])
            laud.begin_fill()
            laud.forward(raadius)
            laud.left(90)
            laud.circle(raadius, nurk)
            laud.left(90)
            laud.goto(0, 0)
            laud.end_fill()

    def joonista_nool():
        nool.clear()
        nool.penup()
        nool.goto(0, raadius + 10)
        nool.pendown()
        nool.goto(0, raadius + 40)
        
    pööre = 0
    kiirus = 100000

    for _ in range(40):
        pööre += kiirus
        joonista_rulet(pööre)
        joonista_nool()
        update()
        sleep(0.05)
        kordaja = randint(100,1000)/1000
        kiirus *= kordaja

    tracer(1)

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

def neeger(sõnum, y_offset=0, viivitus=0.03):
        tekst = ""
        for täht in sõnum:
            tekst += täht
            konto_tekst.goto(-side/2 + 20, side/2 - 60 + y_offset)
            konto_tekst.write(tekst, font=("Courier", 14, "normal"))
            sleep(viivitus)

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

jätka = True
while jätka:
    soovitud_raha = textinput("Väljavõtt", "Palju soovite välja võtta?")

    try:
        soovitud_raha = int(soovitud_raha)
        jätka = False
    except:
        kiri("See ei olnud arv!", -130)
    
if soovitud_raha <= konto:
    konto -= soovitud_raha
    konto_tekst.clear()
    kiri(f"Võtsite {soovitud_raha} € välja!", 30)
    kiri(f"Alles on {konto} €.", -10)
        
    raha = messagebox.askyesno("Küsimus", "Võta raha pangaautomaadist välja? (jah/ei)")
        
    if (raha):
        screen = getscreen()
        screen.addshape("raha.gif")
        p = Turtle()
        p.shape("raha.gif")
        p.resizemode("user")
        p.shapesize(0.5, 0.5)
        p.penup()
        p.goto(0, 0)
       
    else:
        konto_tekst.clear()
        ban = nimi + " has been givin " + str(soovitud_raha) + "€" + " for good behavior"
        kiri("Pangaautomaat: Olgu, ma jätan endale siis", 30)
        sleep(2)
        kiri(nimi + ": Nooooo! Anna tagasi :(", 10)
        sleep(1)
        kiri("Pangaautomaat: Ei...", -10)
        sleep(2)
        kiri(nimi + ": Aga miks?", -30)
        sleep(2)
        kiri("Pangaautomaat: Sa oled ülbe neeger", -50)
        sleep(1.5)
        kiri(nimi + ": Ei mai ole >:(", -70)
        sleep(0.5)
        kiri("User20384: First lol", -90)
        sleep(1.5)
        kiri(nimi + ": Kes see ahv veel on?", -110)
        sleep(2)
        kiri("Pangaautomaat: Hold up, las ma bannin ta", -130)
        sleep(1.75)
        kiri("Server: User20384 got kick reason spamming ", -150)
        sleep(2)
        kiri(nimi + ": Anna mu " + str(soovitud_raha) + "€ ka tagasi nüüd", -170)
        sleep(1.75)
        kiri("Pangaautomaat: No okei, kuna su emme ütles", -190)
        sleep(2)
        neeger("Server: " + ban, -210)
        sleep(1)
        kiri(nimi + ": Yay! Thank you mommy", -230)
        sleep(1.5)
        kiri("Pangaautomaat: Edaspidi oled tubli poiss, eks?", -250)
        sleep(1.75)
        tubli_poiss = messagebox.askyesno("Tähtis küsimus", "Kas sa oled edaspidi tubli poiss? (Jah issi/Ei)")
        konto_tekst.clear()

        if (tubli_poiss):
            kiri("Pangaautomaat: Tublu poiss", 30)
            sleep(1)
            kiri("Pangaautomaat: Võta oma " + str(soovitud_raha) + "€", 10)
            sleep(1.5)
            kiri(nimi + ": Väga äge", -10)
            sleep(1.5)
            konto_tekst.clear()
            screen = Screen()
            screen.addshape("good.gif")
            p = Turtle()
            p.shape("good.gif")
            p.resizemode("user")
            p.penup()
            p.goto(0, 0)
            
        else:
            kiri("Pangaautomaat: ...", 30)
            sleep(2)
            kiri("Pangaautomaat: Mida vittu sa ütlesid mulle?", 10)
            sleep(2.5)
            kiri(nimi + ": Ma ei ole su issi🗣️💢💢", -10)
            sleep(1.75)
            kiri("Pangaautomaat: Kuradi loll neeger", -30)
            sleep(2)
            kiri("Pangaautomaat: Saad banni!", -50)
            sleep(0.75)
            neeger(nimi + ": EIIIIIII!", -70)
            sleep(1.75)
            kiri("Server: " + nimi + " data has been stolen", -90)
            sleep(0.25)
            kiri("Server: " + nimi + " " + str(konto) + "€ has been taken away", -110)
            sleep(0.25)
            kiri("Server: " + nimi + " nudes has been leaked", -130)
            sleep(0.25)
            kiri(nimi + ": WHAT?", -150)
            sleep(2)
            kiri("Server: " + nimi + " home location has been leaked", -170)
            sleep(0.25)
            kiri("Server: 58.230461, 26.449073", -190)
            sleep(0.25)
            kiri("Server: " + str(soovitud_raha) + "€ Has been taken back", -210)
            sleep(0.25)
            kiri(nimi + ": DUDE NOOOOOOO!", -230)
            sleep(2)
            kiri("Pangaautomaat: Its over mees", -250)
            sleep(3)
            konto_tekst.clear()
            screen = Screen()
            screen.addshape("bad.gif")
            p = Turtle()
            p.shape("bad.gif")
            p.resizemode("user")
            p.penup()
            p.goto(0, 0)

else:
    kiri("Kontol on liiga vähe raha!", -130)

    casino = messagebox.askyesno("Kasiino", "Kas soovite teenida raha juurde?")

    casino = messagebox.askyesno("Kasiino", "Kas soovite teenida raha juurde?")

    if casino:
        kasutaja_valik = textinput("Kasiino", "Red (1) või Black (2)?")
        konto_tekst.clear()
        try:
            kasutaja_valik = int(kasutaja_valik)
            display_animation_casino()
        except:
            kiri("Vale sisestus!", -190)
            exitonclick()

        suvaline_arv = randint(1, 2)
        konto_tekst.clear()
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
        konto_tekst.clear()
        kiri("Ole vaene rott edasi siis...", 20)
        
exitonclick()

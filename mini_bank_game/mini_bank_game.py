#from import kaka siin, ALALALALA!
from turtle import *
from random import randint
from tkinter import messagebox
from time import sleep
import sqlite3

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
    laud.clear()
    nool.clear()
    update()
    

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

def neeger(sõnum, y_offset=0, viivitus=0.03):
        tekst = ""
        for täht in sõnum:
            tekst += täht
            konto_tekst.goto(-side/2 + 20, side/2 - 60 + y_offset)
            konto_tekst.write(tekst, font=("Courier", 14, "normal"))
            sleep(viivitus)

def kiri(sõnum, y_offset=0):
    konto_tekst.goto(-side/2 + 20, side/2 - 60 + y_offset)
    konto_tekst.write(sõnum, font=("Courier", 14, "normal"))

teade = Turtle()
teade.hideturtle()
teade.penup()
teade.goto(-side/2 + 20, side/2 - 90)
teade.color("black")

conn = sqlite3.connect("pank.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS kasutajad (
    nimi TEXT PRIMARY KEY,
    pin TEXT,
    saldo INTEGER
)
""")

def salvesta_konto(nimi, kood1, konto):
    cursor.execute("""
    INSERT INTO kasutajad (nimi, pin, saldo)
    VALUES (?, ?, ?)
    ON CONFLICT(nimi) DO UPDATE SET
        pin=excluded.pin,
        saldo=excluded.saldo
    """, (nimi, kood1, konto))

    conn.commit()

kiri("Tere tulemast pangaautomaati!", 30)
tegemata = True

kontinuu = True
while kontinuu:
    # seda osa teeme ainult ühe korra
    
    if tegemata:
        konto_olemas = messagebox.askyesno("Konto", "Kas teil on juba konto olemas?")

        if konto_olemas:
            nimi = textinput("Nimi", "Sisesta nimi:")

            cursor.execute("SELECT * FROM kasutajad WHERE nimi = ?", (nimi,))
            tulemus = cursor.fetchone()

            if tulemus:
                nimi, kood1, konto = tulemus

                katsed = 3
                sisse_logitud = False

                while katsed > 0:
                    sisestatud_pin = textinput("PIN", "Sisesta PIN:")

                    if sisestatud_pin == kood1:
                        kiri(f"Tere, {nimi}!", -20)
                        kiri(f"Teie kontol on {konto} €.", -40)
                        sisse_logitud = True
                        break
                    else:
                        katsed -= 1
                        kiri(f"Vale PIN! Alles jäänud: {katsed}", -30)

                if not sisse_logitud:
                    kiri("Konto lukustatud!", -50)
                    exitonclick()

            else:
                kiri("Kasutajat ei leitud!", -10)
                exitonclick()

        else:
            nimi = textinput("Nimi", "Valige endale kasutajanimi:")
            kood1 = textinput("PIN", "Valige 4-kohaline PIN:")
            konto = 100
            salvesta_konto(nimi, kood1, konto)

            konto_tekst.clear()
            kiri("Pangaautomaat", 20)
            kiri(f"Tere, {nimi}!", -20)
            kiri(f"Teie kontol on {konto} €.", -60)
    tegemata = False

    soovitud_raha = textinput("Väljavõtt", "Palju soovite välja võtta?")

    try:
        soovitud_raha = int(soovitud_raha)
    except:
        kiri("See ei olnud arv!", -130)

    if soovitud_raha > 0 and soovitud_raha <= konto:
        konto -= soovitud_raha
        konto_tekst.clear()
        salvesta_konto(nimi, kood1, konto)
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
            sleep(3)
            p.clear()
            p.hideturtle()
    
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

                konto += int(soovitud_raha)
                salvesta_konto(nimi, kood1, konto)
                konto_tekst.clear()

                screen = Screen()
                screen.addshape("good.gif")
                p = Turtle()
                p.shape("good.gif")
                p.resizemode("user")
                p.penup()
                p.goto(0, 0)
                sleep(3)
                p.clear()
                p.hideturtle()
                
                
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
                sleep(2)

                konto -= int(soovitud_raha)
                salvesta_konto(nimi, kood1, konto)

                konto_tekst.clear()
                screen = Screen()
                screen.addshape("bad.gif")
                p = Turtle()
                p.shape("bad.gif")
                p.resizemode("user")
                p.penup()
                p.goto(0, 0)
                sleep(3)
                p.clear()
                p.hideturtle()

    else:
        kiri("Kontol on liiga vähe raha!", -130)

        casino = messagebox.askyesno("Kasiino", "Kas soovite teenida raha juurde?")

        if casino:
            kasutaja_valik = textinput("Kasiino", "Red (1) või Black (2)?")
            bet_input = int(textinput("Kasiino", "Palju te soovite panustada?"))
            konto_tekst.clear()
            try:
                kasutaja_valik = int(kasutaja_valik)
                bet = int(bet_input)
                display_animation_casino()
            except:
                kiri("Vale sisestus!", -190)
                exitonclick()

            suvaline_arv = randint(1, 2)
            konto_tekst.clear()
            if kasutaja_valik == suvaline_arv:
                konto += bet
                salvesta_konto(nimi, kood1, konto)
                kiri(f"BIG WIN! Te võitsid Paksu Rihardi ja " + str(bet) + "€", 20)
                kiri(f"Teie kontol on nüüd {konto}€ ja Paks Rihard.", -20)
                screen = getscreen()
                screen.addshape("lel.gif")
                p = Turtle()
                p.shape("lel.gif")
                p.resizemode("user")
                p.shapesize(0.5, 0.5)
                p.penup()
                p.goto(0, 0)
                sleep(3)
                p.clear()
                p.hideturtle()

            else:
                konto -= bet
                salvesta_konto(nimi, kood1, konto)
                kiri("Sa kaotasid " + str(bet) + "€ :(", 20)
                screen = getscreen()
                screen.addshape("bob.gif")
                p = Turtle()
                p.shape("bob.gif")
                p.resizemode("user")
                p.shapesize(0.5, 0.5)
                p.penup()
                p.goto(0, 0)
                sleep(3)
                # lisa video
                p.clear()
                p.hideturtle()
        else:
            konto_tekst.clear()
            sleep(1)
            kiri("Pangaautomat: ...?", 30)
            sleep(2)
            kiri("Pangaautomaat: Kas sa tahad tööle minna?", 10)
            sleep(2)
            töö = messagebox.askyesno("Töötu kassa", "Soovite tööle minna?")

            if töö == True:
                konto_tekst.clear()
                kiri("Sul on töö nüüd",30)
                sleep(2)
                import mcdonalds_vaade
                from turtle import *
                mcdonalds_vaade
                
                exitonclick()
            else:
                konto_tekst.clear()
                sleep(1.5)
                kiri("Pangaautomaat: päriselt v?", 30)
                sleep(3)
                kiri(nimi + ": Mida?",10)
                sleep(2)
                kiri("Pangaautomaat: Ma ütlen emmele", -10)
                sleep(1)
                kiri(nimi + ": EIIIIIII!", -30)
                sleep(3)
                kiri("Su ema: Mis see sitt on mis ma kuulen?", -50)
                sleep(1.5)
                kiri("Su ema: Et minu laps ei taha tööle minna", -70)
                sleep(2)
                kiri(nimi + ": Aga emme...", -90)
                sleep(1.5)
                kiri("Su ema: VAIT! " + nimi + "!", -110)
                sleep(1.75)
                kiri("Su ema: Sa lähed pessu", -130)
                sleep(1.5)
                kiri(nimi + ": EIIIIIIIII!!!!!!!!!!", -150)
                sleep(1.75)
                konto_tekst.clear()

                kiri("Sa läksid pessu", 30)
                screen = getscreen()
                screen.addshape("shower.gif")
                p = Turtle()
                p.shape("shower.gif")
                p.resizemode("user")
                p.shapesize(0.5, 0.5)
                p.penup()
                p.goto(0, 0)
                sleep(3)
                p.clear()
                p.hideturtle()

    konto_tekst.hideturtle()
    konto_tekst.clear()
    kiri("Pangaautomaat", 20)
    kiri(f"Tere, {nimi}!", -20)
    kiri(f"Teie kontol on {konto} €.", -60)
    
    jätka_samm = messagebox.askyesno("Pangaautomaat", "Kas soovite teist tehingut teha?")
    if not jätka_samm:
        kontinuu = False
        konto_tekst.clear()
        kiri("Headaega!", 30)
    
exitonclick()

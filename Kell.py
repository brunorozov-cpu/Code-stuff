from tkinter import *
from math import *
import time

raam = Tk()
raam.title("Kell")

w, h = 500, 500
tahvel = Canvas(raam, width=w, height=h)
tahvel.pack()

# Pilt 
taust = PhotoImage(file="taust.png")

# Pilt kellal
tahvel.create_image(w/2, h/2, image=taust)

# Kella raam
tahvel.create_oval(10, 10, w-10, h-10)
tahvel.create_oval(w/2-5, h/2-5, w/2+5, h/2+5, fill="black")

# Numbrid
r_numbrid = min(w/2, h/2) - 50
for i in range(1, 13):
    nurk = pi/2 - i/12 * 2*pi
    x = w/2 + r_numbrid * cos(nurk)
    y = h/2 - r_numbrid * sin(nurk)
    tahvel.create_text(x, y, text=str(i), font=("Arial", 20, "bold"), fill="white")

# Osutid
sek_id = tahvel.create_line(w/2, h/2, w/2, 20, fill="green", width=1)
min_id = tahvel.create_line(w/2, h/2, w/2, 20, fill="yellow", width=3)
tun_id = tahvel.create_line(w/2, h/2, w/2, 20, fill="red", width=5)


def uuenda():
    aeg = time.localtime()
    sekundid = aeg.tm_sec
    minutid = aeg.tm_min
    tund = aeg.tm_hour % 12

    r_sek = min(w/2, h/2) - 30
    r_min = r_sek * 0.8
    r_tun = r_sek * 0.55

    # Sekundiosuti
    x = r_sek * cos(pi/2 - sekundid / 60.0 * 2 * pi)
    y = -r_sek * sin(pi/2 - sekundid / 60.0 * 2 * pi)

    # Minutiosuti
    xm = r_min * cos(pi/2 - (minutid + sekundid/60.0) / 60.0 * 2 * pi)
    ym = -r_min * sin(pi/2 - (minutid + sekundid/60.0) / 60.0 * 2 * pi)

    # Tundiosuti
    xt = r_tun * cos(pi/2 - (tund + minutid/60.0) / 12.0 * 2 * pi)
    yt = -r_tun * sin(pi/2 - (tund + minutid/60.0) / 12.0 * 2 * pi)

    tahvel.coords(sek_id, w/2, h/2, w/2 + x, h/2 + y)
    tahvel.coords(min_id, w/2, h/2, w/2 + xm, h/2 + ym)
    tahvel.coords(tun_id, w/2, h/2, w/2 + xt, h/2 + yt)

    raam.after(1000, uuenda)


uuenda()

raam.mainloop()

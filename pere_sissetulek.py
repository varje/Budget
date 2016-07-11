def neto(bruto):
    maksuvaba = 154
    if (float(bruto) <= float(maksuvaba)):
        return bruto
    else:
        maksustatav = float(bruto) - maksuvaba
        return maksustatav * 0.80 + maksuvaba

ühe_lapse_toetus=45

from tkinter import *
from tkinter import ttk

raam = Tk()
raam.title("Pere sissetulek")
tahvel = Canvas(raam, width=300, height=600)
tahvel.grid()

silt = ttk.Label(raam, text="Ema bruto(€):")
silt.place(x=5, y=5)

emapalk = ttk.Entry(raam)
emapalk.place(x=100, y=5, width=50)

silt = ttk.Label(raam, text="Isa bruto(€):")
silt.place(x=5, y=30)

isapalk = ttk.Entry(raam)
isapalk.place(x=100, y=30, width=50)

silt = ttk.Label(raam, text="Lapsi(tk):")
silt.place(x=5, y=55)

lapsi= ttk.Entry(raam)
lapsi.place(x=100, y=55, width=50)


def arvuta():
    sissetulek = float(neto(emapalk.get())) + float(neto(isapalk.get()))+ float(lapsi.get()) * ühe_lapse_toetus
    silt = ttk.Label(raam, text=("Sissetulek(€):", sissetulek),font=("Helvetica", 14))
    silt.place(x=5, y=130)
    silt = ttk.Label(raam, text=("*Ema(neto,€):", neto(emapalk.get())), foreground='blue')
    silt.place(x=5, y=160)
    silt = ttk.Label(raam, text=('*Isa(neto,€):', neto(isapalk.get())), foreground='red')
    silt.place(x=5, y=180)
    silt = ttk.Label(raam, text=("*Lastetoetus(€):", (float(lapsi.get()) * ühe_lapse_toetus)), foreground='green')
    silt.place(x=5, y=200)
    xy = 5, 220, 280, 495
    isapalk_kraadides=float(neto(isapalk.get()))*360/sissetulek
    emapalk_kraadides=float(neto(emapalk.get()))*360/sissetulek
    lastetoetus_kraadides=(float(lapsi.get()) * ühe_lapse_toetus)*360/sissetulek
    tahvel.create_arc(xy, start=0, extent=emapalk_kraadides, fill="blue")
    tahvel.create_arc(xy, start=emapalk_kraadides, extent= isapalk_kraadides, fill="red")
    tahvel.create_arc(xy, start=(emapalk_kraadides+isapalk_kraadides), extent=lastetoetus_kraadides, fill="green")
nupp = ttk.Button(raam, text="Arvuta", command=arvuta)
nupp.place(x=70, y=90, width=150)
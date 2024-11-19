from tkinter import *
from tkinter.ttk import *
from ZH_Modul import *
from BA_Modul import *

ablak = Tk()
ablak.title("Napló App")
ablak.geometry("320x200")
szoveg0 = Label(ablak,text="")
szoveg = Label(ablak, text="Ha már van fiókja, kérem jelentkezzen be:")
szoveg2 = Label(ablak,text="Ha még nincs fiókja, kérem regisztráljon:")
szoveg3 = Label(ablak,text="")
gombbelepes = Button(ablak, text="Bejelentkezés")
gombregisztracio = Button(ablak,text="Regisztráció")
szoveg0.grid(row=0,column=0)
szoveg.grid(row=1,column=0,sticky=W,pady=2)
szoveg2.grid(row=3,column=0, sticky=W,pady=2)
szoveg3.grid(row=2,column=0)
gombbelepes.grid(row=1,column=1,sticky=E,pady=2)
gombregisztracio.grid(row=3,column=1,sticky=E,pady=2)
mainloop()
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

szoveg0.grid(row=0,column=0,sticky=W,pady=2)
szoveg.grid(row=1,column=0,sticky=W,pady=2)
szoveg2.grid(row=3,column=0, sticky=W,pady=2)
szoveg3.grid(row=2,column=0,sticky=W,pady=2)

def Bejelentkezes():
    belepablak = Toplevel(ablak)
    belepablak.geometry("320x200")
    belepablak.title("Bejelentkezés")

    email_cim = StringVar()
    email_label = Label(belepablak, text="Kérem adja meg az e-mail címét: ")
    email_input = Entry(belepablak, textvariable=email_cim)
    email_label.grid(row=0,column=0)
    email_input.grid(row=0,column=1)
    def em():
        belepes(email_cim)
    tovabbgomb=Button(belepablak, text="Tovább", command=em)
    tovabbgomb.grid(row=1,column=0)
    belepablak.mainloop()

def Regisztralas():
    regablak = Toplevel(ablak)
    regablak.geometry("320x200")
    regablak.title("Regisztráció")
    regablak.mainloop()

gombbelepes = Button(ablak, text="Bejelentkezés", command=Bejelentkezes)
gombregisztracio = Button(ablak,text="Regisztráció", command=Regisztralas)

gombbelepes.grid(row=1,column=1,sticky=E,pady=2)
gombregisztracio.grid(row=3,column=1,sticky=E,pady=2)

ablak.mainloop()
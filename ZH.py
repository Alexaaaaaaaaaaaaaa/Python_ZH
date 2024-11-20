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
szoveg4 = Label(ablak,text="Napló megnyitása:")
szoveg3 = Label(ablak,text="")
szoveg5 = Label(ablak,text="")

szoveg0.grid(row=0,column=0,sticky=W,pady=2)
szoveg.grid(row=1,column=0,sticky=W,pady=2)
szoveg2.grid(row=3,column=0, sticky=W,pady=2)
szoveg3.grid(row=2,column=0,sticky=W,pady=2)
szoveg4.grid(row=5,column=0,sticky=W,pady=2)
szoveg5.grid(row=4,column=0,sticky=W,pady=2)

def Bejelentkezes():
    belepablak = Toplevel(ablak)
    belepablak.geometry("320x200")
    belepablak.title("Bejelentkezés")

    email_cim = StringVar()
    felh_jelszo = StringVar()
    email_label = Label(belepablak, text="Kérem adja meg az e-mail címét: ")
    email_input = Entry(belepablak, textvariable=email_cim)
    jelszo_label = Label(belepablak, text="Kérem adja meg a jelszavát: ")
    jelszo_input = Entry(belepablak, textvariable=felh_jelszo)
    email_label.grid(row=0,column=0)
    email_input.grid(row=0,column=1)
    jelszo_label.grid(row=1, column=0)
    jelszo_input.grid(row=1, column=1)
    def em():
        belepes(email_cim,felh_jelszo)
    tovabbgomb=Button(belepablak, text="Tovább", command=em)
    tovabbgomb.grid(row=2,column=1)
    belepablak.mainloop()

def Regisztralas():
    regablak = Toplevel(ablak)
    regablak.geometry("320x200")
    regablak.title("Regisztráció")
    email_cim = StringVar()
    reg_jelszo = StringVar()
    email_label = Label(regablak, text="Kérem adja meg az e-mail címét: ")
    email_input = Entry(regablak, textvariable=email_cim)
    jelszo_label = Label(regablak, text="Kérem adja meg a jelszavát: ")
    jelszo_input = Entry(regablak, textvariable=reg_jelszo)
    email_label.grid(row=0, column=0)
    email_input.grid(row=0, column=1)
    jelszo_label.grid(row=1, column=0)
    jelszo_input.grid(row=1, column=1)

    def Reg():
        regisztracio(email_cim,reg_jelszo)

    reggomb = Button(regablak, text="Regisztrálok!", command=Reg)
    reggomb.grid(row=2, column=1)
    regablak.mainloop()

def Naplo():
    naploablak = Toplevel(ablak)
    naploablak.geometry("320x200")
    naploablak.title("Napló")

    naploablak.mainloop()

gombbelepes = Button(ablak, text="Bejelentkezés", command=Bejelentkezes)
gombregisztracio = Button(ablak,text="Regisztráció", command=Regisztralas)
gombnaplo = Button(ablak, text="Megnyitás", command=Naplo)

gombbelepes.grid(row=1,column=1,sticky=E,pady=2)
gombregisztracio.grid(row=3,column=1,sticky=E,pady=2)
gombnaplo.grid(row=5,column=1,sticky=E,pady=2)

ablak.mainloop()
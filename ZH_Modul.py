from tkinter import *
from tkinter import messagebox

from prompt_toolkit.shortcuts import message_dialog


def email(_email_cim):
    while " " in _email_cim.get() or "@" not in _email_cim.get() or "." not in _email_cim.get():
        messagebox.showinfo("Hiba","Érvénytelen e-mail!")
        if " " in _email_cim.get():
            messagebox.showinfo("Hiba","Szóközt használt az e-mail címben!")
        elif "@" not in _email_cim.get():
            messagebox.showinfo("Hiba","Kihagyta a @ jelet!")
        else:
            messagebox.showinfo("Hiba","Kihagyta a .-ot!")
            #emailLabel = Label(text="Kérem adja meg az e-mail címét: ")
    return _email_cim

def jelszo_ellenorzes(jelszo):
    ok = False
    proba = 0
    while True:
        jelszo2 = input("Kérem ismét a jelszavát: ")
        if (jelszo == jelszo2):
            ok = True
            break
        else:
            proba +=1
            print("Rossz jelszót adott meg!")
            if (proba == 3):
                break
    return ok

def regisztracio(_jelszo_input):
    def jelszo_bekeres(hosszusag):
        def hossz(_jelszo,min_hossz):
            ok = True
            if len(_jelszo) < min_hossz:
                ok = False
            return ok
        def szamjegyek(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.isnumeric():
                    ok = True
                    break
            return ok
        def kisbetu(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.islower:
                    ok = True
                    break
            return ok
        def nagybetu(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.isupper:
                    ok = True
                    break
            return ok

        #jelszo = input("Kérem adjon meg egy jelszót: ")
        jelszo = _jelszo_input
        while not hossz(jelszo, hosszusag) or not szamjegyek(jelszo) or not kisbetu(jelszo) or not nagybetu(jelszo):
            messagebox.showinfo("Hiba","A jelszó nem megfelelő!")
            jelszo = _jelszo_input
            #jelszo = input("Kérem adjon meg egy jelszót (tartalmazzon kis- és nagybetűt, valamint számot): ")
        return jelszo

    def felhasznalo_mentes(email, jelszo):
        with open("felhasznalok.txt", "a", encoding="utf-8") as fajl:
            fajl.write(email + ";" + jelszo + "\n")

    felhasznalo_email = email()
    felhasznalo_jelszava = jelszo_bekeres()
    ok = jelszo_ellenorzes(felhasznalo_jelszava)
    if ok:
        felhasznalo_mentes(felhasznalo_email,felhasznalo_jelszava)
    return ok


def belepes(_email_cim):
    #belepablak = Tk()
    #belepablak.title("Belépés")
    #_email_cim = StringVar()
    #emailLabel = Label(belepablak, text="Kérem adja meg az e-mail címét: ")
    #_email_cim2 = Entry(belepablak, textvariable=_email_cim)
    #emailLabel.grid(row=0,column=0)
    #_email_cim2.grid(row=0,column=1)
    #def lepes(lep):
    #    return lep
    #tovabb_gomb = Button(belepablak, text="Tovább",command=lepes(True))
    def felhasznalo():
        jelszo = False
        felh_email = email(_email_cim)
        with open("felhasznalok.txt","r",encoding="utf-8") as fajl:
            for sor in fajl:
                felhasznaloi_adatok = sor.strip().split(";")
                if felhasznaloi_adatok[0] == email:
                    jelszo = felhasznaloi_adatok[1]
                break
        return jelszo

    def jelszoellenorzes(_jelszo):
        ok = False
        if jelszo_ellenorzes(_jelszo):
            ok = True
        return ok

    jelszo = felhasznalo()
    if not jelszo:
        messagebox.showinfo("Hiba","Nem regisztrált felhasználó!")
    else:
        if jelszoellenorzes(jelszo):
            print("Belépés..")
        else:
            messagebox.showinfo("Hiba","Rossz jelszót adott meg!")
def email():
    _email_cim = input("Kérem adja meg az e-mail címét: ")
    while " " in _email_cim or "@" not in _email_cim or "." not in _email_cim:
        print("Érvénytelen e-mail!")
        if " " in _email_cim:
            print("Szóközt használt az e-mail címben!")
        elif "@" not in _email_cim:
            print("Kihagyta a @ jelet!")
        else:
            print("Kihagyta a .-ot!")
        _email_cim = input("Kérem adja meg az e-mail címét: ")
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

def regisztracio():
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

        jelszo = input("Kérem adjon meg egy jelszót: ")
        while not hossz(jelszo, hosszusag) or not szamjegyek(jelszo) or not kisbetu(jelszo) or not nagybetu(jelszo):
            print("A jelszó nem megfelelő!")
            jelszo = input("Kérem adjon meg egy jelszót (tartalmazzon kis- és nagybetűt, valamint számot): ")
        return jelszo

    #def valami():


#def belepes():
 #   def felhasznalo():
  #      jelszo = False
   #     email = email()
    #    with open()
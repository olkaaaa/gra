import random

def wprowadzenie():
    print("Witaj w grze 'Walka'!")
    print("Twoim zadaniem jest pokonać złodziei.")
    print("Będziesz musiał walczyć o swoje życie.")
    print("Każda walka może być twoją ostatnią. Powodzenia!\n")

def stworz_bohatera():
    print("Stwórz swojego bohatera!")
    imie = input("Wpisz imię swojego bohatera: ")
    bohater = {
        "imie": imie,
        "zycie": 100,
        "atak_min": 10,
        "atak_max": 20,
        "mana": 50,  
    }
    print(f"\nTwój bohater: {bohater['imie']}, Życie: {bohater['zycie']}, Atak: {bohater['atak_min']}-{bohater['atak_max']}, Mana: {bohater['mana']}\n")
    return bohater

def stworz_przeciwnika():
    przeciwnik_nazwa = random.choice(["Goblina", "Złodzieja", "Orka", "Trolla", "Wampira", "Bandytę"])
    przeciwnik_zycie = random.randint(30, 60)
    przeciwnik_atak_min = random.randint(5, 15)
    przeciwnik_atak_max = random.randint(10, 20)

    przeciwnik = {
        "nazwa": przeciwnik_nazwa,
        "zycie": przeciwnik_zycie,
        "atak_min": przeciwnik_atak_min,
        "atak_max": przeciwnik_atak_max
    }
    return przeciwnik

def stworz_bossa():
    boss = {
        "nazwa": "Mega Boss",
        "zycie": 150,
        "atak_min": 15,
        "atak_max": 50
    }
    return boss

def atak_bohatera(bohater, przeciwnik):
    atak = random.randint(bohater['atak_min'], bohater['atak_max'])
    print(f"\n{bohater['imie']} zadaje przeciwnikowi {atak} obrażeń.")
    przeciwnik["zycie"] -= atak
    print(f"Przeciwnik ma teraz {przeciwnik['zycie']} życia.")

def super_atak(bohater, przeciwnik):
    if bohater["mana"] >= 15:
        atak = random.randint(30, 40)
        print(f"\n{bohater['imie']} używa Super Ataku i zadaje {atak} obrażeń!")
        przeciwnik["zycie"] -= atak
        bohater["mana"] -= 15
        print(f"Przeciwnik ma teraz {przeciwnik['zycie']} życia.")
        print(f"Pozostało {bohater['mana']} many.")
    else:
        print("\nNie masz wystarczająco many na Super Atak!")

def podwojny_atak(bohater, przeciwnik):
    if bohater["mana"] >= 10:
        atak1 = random.randint(bohater['atak_min'], bohater['atak_max'])
        atak2 = random.randint(bohater['atak_min'], bohater['atak_max'])
        print(f"\n{bohater['imie']} wykonuje Podwójny Atak: {atak1} i {atak2} obrażeń!")
        przeciwnik["zycie"] -= (atak1 + atak2)
        bohater["mana"] -= 10
        print(f"Przeciwnik ma teraz {przeciwnik['zycie']} życia.")
        print(f"Pozostało {bohater['mana']} many.")
    else:
        print("\nNie masz wystarczająco many na Podwójny Atak!")

def atak_przeciwnika(przeciwnik, bohater):
    atak = random.randint(przeciwnik['atak_min'], przeciwnik['atak_max'])
    print(f"\nPrzeciwnik {przeciwnik['nazwa']} zadaje ci {atak} obrażeń.")
    bohater["zycie"] -= atak
    print(f"Masz teraz {bohater['zycie']} życia.")

def spotkanie_z_wedrowcem(bohater):
    print("\nSpotykasz wędrowca na drodze.")
    print("Wędrowiec chce ci pomoc!")
    
    wybor = input("Czy chcesz przyjąć pomoc? (tak/nie): ")
    
    if wybor == "tak":
        przedmiot = random.choice(["miksturę życia", "miksturę many", "magiczny amulet"])
        print(f"Wędrowiec daje ci {przedmiot}.")
        
        if przedmiot == "miksturę życia":
            bohater["zycie"] += 50
            print(f"Twoje życie wzrosło do {bohater['zycie']}.")
        elif przedmiot == "miksturę many":
            bohater["mana"] += 30
            print(f"Twoja mana wzrosła do {bohater['mana']}.")
        elif przedmiot == "magiczny amulet":
            bohater["atak_min"] += 5
            bohater["atak_max"] += 5
            print(f"Twój atak wzrósł do {bohater['atak_min']}-{bohater['atak_max']}.")
    else:
        print("Odrzucasz pomoc wędrowca i kontynuujesz swoją podróż.") 

def skrzynia(bohater):
    print("\nPrzed ważną bitwą docierasz na szczyt góry. Tam znajduje się ukryte miejsce.")
    print("W tym tajemniczym miejscu znajduje się stara skrzynia.")
    
    wybor = input("Czy chcesz otworzyć skrzynię? (tak/nie): ").lower()
    
    if wybor == "tak":
        przedmiot = random.choice(["legendarny miecz", "złoty pierścień", "zatruty kielich"])
        print(f"Z krzyni dostajesz: {przedmiot}!")

        if przedmiot == "legendarny miecz":
            bohater["atak_min"] += 10
            bohater["atak_max"] += 10
            print(f"Twoje ataki zostały wzmocnione! Nowy atak: {bohater['atak_min']}-{bohater['atak_max']}.")
        elif przedmiot == "złoty pierścień":
            bohater["zycie"] += 100
            print(f"Twoje życie zostało przywrócone do {bohater['zycie']}.")
        elif przedmiot == "zatruty kielich":
            bohater["zycie"] -= 30
            print(f"Zatrucie! Twoje życie spadło do {bohater['zycie']}.")
            return True  
    else:
        print("Nie otwierasz skrzyni i kontynuujesz swoją podróż.")

    return False   

def walka(bohater, przeciwnik):
    print(f"\nSpotykasz przeciwnika: {przeciwnik['nazwa']} (Życie: {przeciwnik['zycie']})")
    print("\nKwestia przed walką:")
    print(f"Przeciwnik: 'Ha! Nie pokonaz mnie.'")

    while bohater["zycie"] > 0 and przeciwnik["zycie"] > 0:
        print("\nOpcje:")
        print("1. Atak")
        print("2. Super Atak (kosztuje 15 many)")
        print("3. Podwójny Atak (kosztuje 10 many)")
        print("4. Ucieczka")

        wybor = input("Co robisz? (1/2/3/4): ")

        if wybor == "1":
            atak_bohatera(bohater, przeciwnik)
            if przeciwnik["zycie"] > 0:
                atak_przeciwnika(przeciwnik, bohater)
        elif wybor == "2":
            super_atak(bohater, przeciwnik)
            if przeciwnik["zycie"] > 0:
                atak_przeciwnika(przeciwnik, bohater)
        elif wybor == "3":
            podwojny_atak(bohater, przeciwnik)
            if przeciwnik["zycie"] > 0:
                atak_przeciwnika(przeciwnik, bohater)
        elif wybor == "4":
            print("Uciekasz z walki!")
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

    if bohater["zycie"] <= 0:
        print("\nNiestety, zostałeś pokonany. Gra skończona.")
        return False
    elif przeciwnik["zycie"] <= 0:
        print(f"\nPokonałeś przeciwnika: {przeciwnik['nazwa']}!")
        return True

def gra():
    wprowadzenie()
    bohater = stworz_bohatera()

    while bohater["zycie"] > 0:
        if random.random() < 1:  
            spotkanie_z_wedrowcem(bohater)
        przeciwnik = stworz_przeciwnika()
        if not walka(bohater, przeciwnik):
            break  

        print("\nWyruszasz dalej na przygodę...")

    if bohater["zycie"] > 0:
        print("\nGratulacje! Pokonałeś wszystkich przeciwników!")

        boss = stworz_bossa()
        if random.random() < 1:  
            skrzynia(bohater)
        print(f"\nTeraz stajesz twarzą w twarz z bossem: {boss['nazwa']}! (Życie: {boss['zycie']})")
        if walka(bohater, boss):
            print("\nZwycięstwo! Pokonałeś bossa!")
        else:
            print("\nNiestety, boss pokonał cię. Gra skończona.")

if __name__ == "__main__":
    gra()
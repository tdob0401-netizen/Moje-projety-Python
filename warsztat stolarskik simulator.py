import random

print("===================================")
print("       SYMULATOR STOLARZA")
print("===================================")

gotowka = 2000.0
dzien = 1
reputacja = 0

magazyn = {
    "sosna": 10,
    "dab": 3,
    "sklejka": 5
}

ceny = {
    "sosna": 20,
    "dab": 60,
    "sklejka": 30
}

meble = {
    "polka": {
        "nazwa": "Półka",
        "material": "sosna",
        "ilosc": 2,
        "koszt_pracy": 40,
        "cena": 180
    },
    "krzeslo": {
        "nazwa": "Krzesło",
        "material": "sosna",
        "ilosc": 3,
        "koszt_pracy": 60,
        "cena": 280
    },
    "stol": {
        "nazwa": "Stół dębowy",
        "material": "dab",
        "ilosc": 4,
        "koszt_pracy": 120,
        "cena": 650
    },
    "szafka": {
        "nazwa": "Szafka",
        "material": "sklejka",
        "ilosc": 4,
        "koszt_pracy": 100,
        "cena": 420
    }
}

zamowienia = []


def pokaz_stan():
    print("\n--- STAN WARSZTATU ---")
    print("Dzień:", dzien)
    print("Gotówka:", round(gotowka, 2), "zł")
    print("Reputacja:", reputacja)
    print("\nMagazyn:")

    for material, ilosc in magazyn.items():
        print(material, "-", ilosc, "szt.")


def kup_drewno():
    global gotowka

    print("\n--- SKŁAD DREWNA ---")

    for material, cena in ceny.items():
        print(material, "-", cena, "zł za sztukę")

    material = input("Co kupujesz? ").lower()

    if material not in ceny:
        print("Nie znam takiego materiału.")
        return

    try:
        ilosc = int(input("Ile sztuk kupujesz? "))
    except ValueError:
        print("Wpisz liczbę całkowitą.")
        return

    if ilosc <= 0:
        print("Liczba musi być większa od zera.")
        return

    koszt = ceny[material] * ilosc

    if koszt > gotowka:
        print("Nie masz wystarczająco pieniędzy.")
        return

    gotowka -= koszt
    magazyn[material] += ilosc

    print("Zakup udany! Koszt:", koszt, "zł")


def pokaz_meble():
    print("\n--- KATALOG MEBLI ---")

    for kod, mebel in meble.items():
        print(
            kod, "-", mebel["nazwa"],
            "| materiał:", mebel["material"],
            "| potrzebujesz:", mebel["ilosc"], "szt.",
            "| cena:", mebel["cena"], "zł"
        )


def wykonaj_mebel():
    global gotowka, reputacja

    pokaz_meble()
    kod = input("\nCo produkujesz? ").lower()

    if kod not in meble:
        print("Nie ma takiego produktu.")
        return

    mebel = meble[kod]
    material = mebel["material"]
    potrzebne = mebel["ilosc"]

    if magazyn[material] < potrzebne:
        print("Za mało materiału:", material)
        print("Kup materiał albo wybierz inny mebel.")
        return

    koszt_pracy = mebel["koszt_pracy"]
    cena = mebel["cena"]

    magazyn[material] -= potrzebne
    gotowka -= koszt_pracy
    reputacja += 1

    zamowienia.append({
        "nazwa": mebel["nazwa"],
        "cena": cena,
        "koszt": koszt_pracy
    })

    print("\nUdało się wykonać:", mebel["nazwa"])
    print("Koszt pracy:", koszt_pracy, "zł")
    print("Mebel czeka na sprzedaż.")


def sprzedaj_mebel():
    global gotowka, reputacja

    if not zamowienia:
        print("Nie masz gotowych mebli na sprzedaż.")
        return

    print("\n--- GOTOWE MEBLE ---")

    for i, mebel in enumerate(zamowienia, start=1):
        print(i, "-", mebel["nazwa"], "-", mebel["cena"], "zł")

    try:
        numer = int(input("Który mebel sprzedajesz? "))
    except ValueError:
        print("Wpisz numer mebla.")
        return

    if numer < 1 or numer > len(zamowienia):
        print("Nie ma takiego numeru.")
        return

    mebel = zamowienia.pop(numer - 1)
    gotowka += mebel["cena"]
    reputacja += 2

    print("Sprzedano:", mebel["nazwa"])
    print("Otrzymujesz:", mebel["cena"], "zł")


def przyjmij_zlecenie():
    print("\n--- ZLECENIE OD KLIENTA ---")

    klienci = [
        ("Sąsiad", "Półka", 180),
        ("Kawiarnia", "3 krzesła", 900),
        ("Rodzina", "Stół dębowy", 850),
        ("Biuro", "Szafka", 500)
    ]

    klient = random.choice(klienci)

    print("Klient:", klient[0])
    print("Potrzebuje:", klient[1])
    print("Proponowana zapłata:", klient[2], "zł")
    print("To oferta fabularna. Produkty wykonujesz osobno.")


def zakoncz_dzien():
    global dzien, gotowka

    koszt_staly = 50
    gotowka -= koszt_staly
    dzien += 1

    print("\nDzień zakończony.")
    print("Koszty utrzymania warsztatu:", koszt_staly, "zł")
    print("Rozpoczyna się kolejny dzień:", dzien)


while True:
    print("\n========== MENU ==========")
    print("1. Stan warsztatu")
    print("2. Kup drewno")
    print("3. Zobacz katalog mebli")
    print("4. Wykonaj mebel")
    print("5. Sprzedaj gotowy mebel")
    print("6. Spotkaj klienta")
    print("7. Zakończ dzień")
    print("0. Wyjdź z gry")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        pokaz_stan()
    elif wybor == "2":
        kup_drewno()
    elif wybor == "3":
        pokaz_meble()
    elif wybor == "4":
        wykonaj_mebel()
    elif wybor == "5":
        sprzedaj_mebel()
    elif wybor == "6":
        przyjmij_zlecenie()
    elif wybor == "7":
        zakoncz_dzien()
    elif wybor == "0":
        print("Dziękujemy za grę w Symulator Stolarza!")
        break
    else:
        print("Nieprawidłowa opcja.")

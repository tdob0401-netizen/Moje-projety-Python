import random
import sqlite3

# --- KONFIGURACJA BAZY DANYCH SQL ---
conn = sqlite3.connect("warsztat.db")
cursor = conn.cursor()

# Tworzymy tabele w bazie, jeśli jeszcze nie istnieją
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stan_gry (
        id INTEGER PRIMARY KEY,
        gotowka REAL,
        dzien INTEGER,
        reputacja INTEGER
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazyn (
        material TEXT PRIMARY KEY,
        ilosc INTEGER
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS zamowienia (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nazwa TEXT,
        cena REAL,
        koszt REAL
    )
""")
conn.commit()

# Jeśli baza jest pusta, wrzucamy stan początkowy
cursor.execute("SELECT COUNT(*) FROM stan_gry")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO stan_gry (id, gotowka, dzien, reputacja) VALUES (1, 2000.0, 1, 0)")
    
    poczatkowy_magazyn = [("sosna", 10), ("dab", 3), ("sklejka", 5)]
    cursor.executemany("INSERT OR IGNORE INTO magazyn (material, ilosc) VALUES (?, ?)", poczatkowy_magazyn)
    conn.commit()


# --- FUNKCJE POMOCNICZE DO BAZY SQL ---

def pobierz_dane_gry():
    cursor.execute("SELECT gotowka, dzien, reputacja FROM stan_gry WHERE id = 1")
    return cursor.fetchone()

def zaktualizuj_dane_gry(gotowka, dzien, reputacja):
    cursor.execute("UPDATE stan_gry SET gotowka = ?, dzien = ?, reputacja = ? WHERE id = 1", (gotowka, dzien, reputacja))
    conn.commit()

def pobierz_magazyn():
    cursor.execute("SELECT material, ilosc FROM magazyn")
    return dict(cursor.fetchall())

def zaktualizuj_magazyn(material, ilosc):
    cursor.execute("UPDATE magazyn SET ilosc = ? WHERE material = ?", (ilosc, material))
    conn.commit()

def pobierz_zamowienia():
    cursor.execute("SELECT id, nazwa, cena, koszt FROM zamowienia")
    rows = cursor.fetchall()
    return [{"id": r[0], "nazwa": r[1], "cena": r[2], "koszt": r[3]} for r in rows]


# --- ORYGINALNA LOGIKA GRY (ZMODYFIKOWANA POD SQL) ---

print("===================================")
print("        SYMULATOR STOLARZA (SQL)")
print("===================================")

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


def pokaz_stan():
    gotowka, dzien, reputacja = pobierz_dane_gry()
    magazyn = pobierz_magazyn()
    
    print("\n--- STAN WARSZTATU (ZAPISANY W SQL) ---")
    print("Dzień:", dzien)
    print("Gotówka:", round(gotowka, 2), "zł")
    print("Reputacja:", reputacja)
    print("\nMagazyn:")

    for material, ilosc in magazyn.items():
        print(material, "-", ilosc, "szt.")


def kup_drewno():
    gotowka, dzien, reputacja = pobierz_dane_gry()
    magazyn = pobierz_magazyn()

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

    # Zapis zmian w bazie SQL
    zaktualizuj_dane_gry(gotowka, dzien, reputacja)
    zaktualizuj_magazyn(material, magazyn[material])

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
    gotowka, dzien, reputacja = pobierz_dane_gry()
    magazyn = pobierz_magazyn()

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

    # Zapis w bazie SQL
    zaktualizuj_dane_gry(gotowka, dzien, reputacja)
    zaktualizuj_magazyn(material, magazyn[material])

    cursor.execute("INSERT INTO zamowienia (nazwa, cena, koszt) VALUES (?, ?, ?)", 
                   (mebel["nazwa"], cena, koszt_pracy))
    conn.commit()

    print("\nUdało się wykonać:", mebel["nazwa"])
    print("Koszt pracy:", koszt_pracy, "zł")
    print("Mebel czeka na sprzedaż (zapisano w bazie SQL).")


def sprzedaj_mebel():
    gotowka, dzien, reputacja = pobierz_dane_gry()
    zamowienia = pobierz_zamowienia()

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

    wybrany = zamowienia[numer - 1]
    
    # Usuwamy z bazy zamówień
    cursor.execute("DELETE FROM zamowienia WHERE id = ?", (wybrany["id"],))
    conn.commit()

    gotowka += wybrany["cena"]
    reputacja += 2

    zaktualizuj_dane_gry(gotowka, dzien, reputacja)

    print("Sprzedano:", wybrany["nazwa"])
    print("Otrzymujesz:", wybrany["cena"], "zł")


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
    gotowka, dzien, reputacja = pobierz_dane_gry()
    koszt_staly = 50
    gotowka -= koszt_staly
    dzien += 1

    zaktualizuj_dane_gry(gotowka, dzien, reputacja)

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
        conn.close()
        break
    else:
        print("Nieprawidłowa opcja.")

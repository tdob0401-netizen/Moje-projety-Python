
print("=== KALKULATOR ZAROBKU ===")

ilosc = int(input("Ile mebli zrobiłeś? "))

cena = float(input("Ile zarabiasz za jeden mebel? "))

czas = float(input("Ile godzin zajmuje wykonanie jednego mebla? "))

zarobek = ilosc * cena
czas_laczny = ilosc * czas

stawka_godzinowa = zarobek / czas_laczny

print("Twój całkowity zarobek:", zarobek, "zł")
print("Łączny czas pracy:", czas_laczny, "godzin")
print("Zarobek na godzinę:", stawka_godzinowa, "zł/h")

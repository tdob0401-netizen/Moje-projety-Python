
import os
print(os.getcwd())

print("=== DZIENNIK TRENINGOWY ===")

# Pobieranie danych
czas = float(input("Ile godzin trenowałeś? "))
dystans = float(input("Ile kilometrów przejechałeś? "))

intensywnosc = input(
    "Jaka była intensywność? (niska/srednia/wysoka): "
)

samopoczucie = input(
    "Jak się czujesz po treningu? (świetnie/dobrze/średnio/słabo): "
)

# Obliczanie średniej prędkości
if czas > 0:
    srednia_predkosc = dystans / czas
else:
    srednia_predkosc = 0

# Wyświetlanie podsumowania
print("\n=== PODSUMOWANIE TRENINGU ===")
print("Czas treningu:", czas, "godz.")
print("Przejechany dystans:", dystans, "km")
print("Intensywność:", intensywnosc)
print("Samopoczucie:", samopoczucie)

if czas > 0:
    print("Średnia prędkość:", round(srednia_predkosc, 2), "km/h")
else:
    print("Nie można obliczyć prędkości, ponieważ czas wynosi 0.")

# Zapisywanie treningu do pliku
with open("treningi.txt", "a", encoding="utf-8") as plik:
    plik.write("=== TRENING ===\n")
    plik.write(f"Czas: {czas} godz.\n")
    plik.write(f"Dystans: {dystans} km\n")
    plik.write(f"Intensywność: {intensywnosc}\n")
    plik.write(f"Samopoczucie: {samopoczucie}\n")

    if czas > 0:
        plik.write(
            f"Średnia prędkość: {round(srednia_predkosc, 2)} km/h\n"
        )

    plik.write("\n")

print("\nTrening zapisany do pliku treningi.txt!")
print("Folder zapisu:", os.getcwd())

input("\nNaciśnij Enter, aby zakończyć...") 

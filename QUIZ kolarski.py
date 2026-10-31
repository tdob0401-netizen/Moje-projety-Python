
print("=" * 35)
print("       QUIZ KOLARSKI")
print("=" * 35)

punkty = 0
poprawne = 0
bledy = 0

# PYTANIE 1
print("\n1. Ile pedałów ma typowy rower?")
print("A) 1")
print("B) 2")
print("C) 3")

odp = input("Twoja odpowiedź: ").upper()

if odp == "B":
    print("Dobra odpowiedź! +1 punkt")
    punkty += 1
    poprawne += 1
else:
    print("Błąd! -1 punkt. Poprawna odpowiedź: B")
    punkty -= 1
    bledy += 1

# PYTANIE 2
print("\n2. Jak nazywa się wyścig dookoła Francji?")
print("A) Tour de France")
print("B) Giro d'Italia")
print("C) Vuelta a España")

odp = input("Twoja odpowiedź: ").upper()

if odp == "A":
    print("Dobra odpowiedź! +1 punkt")
    punkty += 1
    poprawne += 1
else:
    print("Błąd! -1 punkt. Poprawna odpowiedź: A")
    punkty -= 1
    bledy += 1

# PYTANIE 3
print("\n3. Czym zmienia się biegi w rowerze?")
print("A) Hamulcem")
print("B) Przerzutkami")
print("C) Dzwonkiem")

odp = input("Twoja odpowiedź: ").upper()

if odp == "B":
    print("Dobra odpowiedź! +1 punkt")
    punkty += 1
    poprawne += 1
else:
    print("Błąd! -1 punkt. Poprawna odpowiedź: B")
    punkty -= 1
    bledy += 1

# PYTANIE 4
print("\n4. Co mierzy licznik rowerowy?")
print("A) Prędkość lub dystans")
print("B) Poziom paliwa")
print("C) Temperaturę silnika")

odp = input("Twoja odpowiedź: ").upper()

if odp == "A":
    print("Dobra odpowiedź! +1 punkt")
    punkty += 1
    poprawne += 1
else:
    print("Błąd! -1 punkt. Poprawna odpowiedź: A")
    punkty -= 1
    bledy += 1

# PYTANIE 5
print("\n5. Co oznacza skrót MTB?")
print("A) Kolarstwo torowe")
print("B) Kolarstwo górskie")
print("C) Kolarstwo szosowe")

odp = input("Twoja odpowiedź: ").upper()

if odp == "B":
    print("Dobra odpowiedź! +1 punkt")
    punkty += 1
    poprawne += 1
else:
    print("Błąd! -1 punkt. Poprawna odpowiedź: B")
    punkty -= 1
    bledy += 1

# PODSUMOWANIE
print("\n" + "=" * 35)
print("       PODSUMOWANIE QUIZU")
print("=" * 35)

print("Poprawne odpowiedzi:", poprawne)
print("Błędne odpowiedzi:", bledy)
print("Końcowa liczba punktów:", punkty)

procent = poprawne / 5 * 100
print("Poprawność:", round(procent), "%")

if poprawne == 5:
    print("Ocena: PERFEKCYJNIE!")
elif procent >= 80:
    print("Ocena: Świetnie!")
elif procent >= 60:
    print("Ocena: Dobrze!")
elif procent >= 40:
    print("Ocena: Trenuj dalej!")
else:
    print("Ocena: Czas na trening!")

print("=" * 35)
print("Dzięki za udział w quizie!")

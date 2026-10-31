print("=== KALKULATOR ===")

a = float(input("Podaj pierwszą liczbę: "))
operator = input("Wybierz działanie (+, -, *, /): ")
b = float(input("Podaj drugą liczbę: "))

if operator == "+":
    wynik = a + b
elif operator == "-":
    wynik = a - b
elif operator == "*":
    wynik = a * b
elif operator == "/":
    if b != 0:
        wynik = a / b
    else:
        print("Nie można dzielić przez zero!")
        exit()
else:
    print("Nieznane działanie!")
    exit()

print("Wynik:", wynik)

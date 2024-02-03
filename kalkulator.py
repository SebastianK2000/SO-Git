def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y != 0:
        return x / y
    else:
        return "Błąd: Nie można dzielić przez zero"

while True:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Zakończ")

    wybor = input("Podaj numer operacji (1/2/3/4/5): ")

    if wybor == '5':
        print("Koniec programu.")
        break

    if wybor not in ('1', '2', '3', '4'):
        print("Nieprawidłowy wybór. Wybierz operację od 1 do 5.")
        continue

    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))

    if wybor == '1':
        print(f"Wynik: {dodawanie(liczba1, liczba2)}")
    elif wybor == '2':
        print(f"Wynik: {odejmowanie(liczba1, liczba2)}")
    elif wybor == '3':
        print(f"Wynik: {mnozenie(liczba1, liczba2)}")
    elif wybor == '4':
        print(f"Wynik: {dzielenie(liczba1, liczba2)}")

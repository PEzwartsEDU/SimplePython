from unittest import case

print("Welk type procentsom wil je oplossen; maak je keuze:")
print("[1] Hoeveel is x% van y?")
print("[2] Hoeveel % is x van y")
print("[3] x neemt toe met y%; hoeveel heb je nu?")
print("[4] x neemt af met y%; hoeveel heb je nu?")
choice = input("Welke optie kies je?")
match choice:
    case "1":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = (x / 100) * y
        print("De vraag is: hoeveel is " + str(x) + "% van " + str(y) + "?")
        print("Het antwoord is: " + str(answer))
        print("De berekening is: " + str(x) + "% = " + str(x/100) + " en " + str(x/100) + " x " + str(y) + " = " + str(answer) )
    case "2":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = (x / y) * 100
        print(f"De vraag is: hoeveel % is {x} van {y}?")
        print(f"Het antwoord is: {answer}")
        print(f"De berekening is: {x} : {y} = {x/y}; {x/y} x 100 = {answer:.0f}%")
    case "3":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = (1,00 + x) * y
        print(f"De vraag is: hoeveel neemt {x} toe met {y}?")
        print(f"Het antwoord is: {answer}")
    case "4":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = (1,00 - x) * y
        print(f"De vraag is: hoeveel neemt {x} af met {y}?")
        print(f"Het antwoord is: {answer}")

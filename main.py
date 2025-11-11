from unittest import case

print("Welk type procentsom wil je oplossen; maak je keuze:")
print("[1] Hoeveel is x% van y?")
print("[2] Hoeveel % is x van y")
print("[3] De vraag is: hoeveel neemt x toe met y?")
print("[4] De vraag is: hoeveel neemt x af met y?")
print("[5] 326 is toegenomen naar 413; met hoeveel procent is het toegenomen?")
print("[6] 413 is afgenomen naar 326; met hoeveel procent is het afgenomen?")
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
    case "5":
        x = float(input("Wat is x? Hoogste bedrag"))
        y = float(input("Wat is y? Laagste bedrag"))
        answer = (x : y)
        print(f"326 is toegenomen naar 413; met hoeveel procent is het toegenomen?")
        print(f"Het antwoord is: {answer}")
    case "6":
        x = float(input("Wat is x? Laagste bedrag"))
        y = float(input("Wat is y? Hoogste bedrag"))
        answer = (y : x)
        print(f"413 is afgenomen naar 326; met hoeveel procent is het afgenomen?")
        print(f"Het antwoord is: {answer}")
    case "7":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = (x : y)
        print(f"17% is toegenomen naar 654; met hoeveel procent is het toegenomen?")
        print(f"Het antwoord is: {answer}")
    case "8":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = (y : x)
        print(f"17% is afgenomen naar 654; met hoeveel procent is het afgenomen?")
        print(f"Het antwoord is: {answer}")

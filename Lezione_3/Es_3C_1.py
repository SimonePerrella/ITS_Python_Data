#Esercizio 3C-1. Scrivere un programma in Python che utilizzi un match statement per classificare un voto scolastico in base alla scala italiana
#Il programma deve accettare in input un voto numerico intero da 1 a 10 e stampare la valutazione corrispondente:
12

voto = int(input("inserisci un numero: "))

match voto :
    case 10:
        print("Eccellente")
    case 8|9:
        print("Molto buono")
    case 6|7:
        print("Sufficiente")
    case 4|5 :
        print("Insufficiente")
    case 1|2|3 :
        print("Gravemente insufficiente")
    case _:
        print("voto non valido")
    
        



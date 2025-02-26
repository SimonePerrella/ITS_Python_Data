'''
Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, 
espresso come numero intero e usare un match per determinare il corrispondente GPA americano, secondo questa tabella di conversione:

'''
n=int(input("Inserisci il tuo voto di laurea: "))

match n:
    case n if n >= 66 and n <= 110:
        gpa = ((n - 66) / (110 - 66)) * 4.0
        print (f"{gpa :.1f}")
    case _:
        print("Il voto di laurea deve essere compreso tra 66 e 110.")
                                        
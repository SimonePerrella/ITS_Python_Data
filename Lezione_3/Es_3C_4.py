'''
Scrivere un programma in Python che permetta all'utente di inserire il nome di un animale e, 
utilizzando un match statement, identifichi a quale categoria esso appartiene. L'animale deve essere classificato in una delle seguenti categorie:

- Mammiferi: cane, gatto, cavallo, elefante, leone.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco.
- Pesci: squalo, trota, salmone, carpa.

Se l'animale non appartiene a nessuna delle categorie sopra elencate, 
 mostrare un messaggio indicante che il programma non è in grado di classificare l'animale inserito.

Suggerimento: Utilizzare una lista per ognuna della quattro categorie.
'''

a = input("inserisci il nome di un animale: ")
mammiferi = ["cane", "gatto", "cavallo", "elefante", "leone"]
Rettili = [ "serpente", "lucertola", "tartaruga", "coccodrillo"]
Uccelli = [" aquila", "pappagallo", "gufo", "falco"]
Pesci = ["squalo", "trota", "salmone", "carpa"]
match a:
    case a if a == mammiferi[0] or a == mammiferi[1] or a == mammiferi[2] or a == mammiferi[3] or a == mammiferi[4]:
        print(f"L'animale: {a} è un mammifero")
    case a if a == Rettili[0] or a == Rettili[1] or a == Rettili[2] or a == Rettili[3]:
        print(f"L'animale: {a} è un Rettile")
    case a if a == Uccelli[0] or  a == Uccelli[1] or  a == Uccelli[2] or  a == Uccelli[3] :
        print(f"L'animale: {a} è un Uccello")
    case a if a == Pesci[0] or a == Pesci[1] or a == Pesci[2] or a == Pesci[3] :
            print(f"L'animale: {a} è un Pesce")
    case _:
          print("il programma non è in grado di classificare l'animale inserito")
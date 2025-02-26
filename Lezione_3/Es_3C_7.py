#Esercizio 3C-7. Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
#Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
#Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".
# Inizializza le variabili
# Inizializza le variabili

t = 0  # numero di teste
c = 0  # numero di croci

# Fai 8 lanci
for _ in range(8):
    # Prendi l'input dall'utente
    lancio_moneta = input("Inserisci t per testa o c per croce: ").strip().lower()
    
    # Usa match per verificare l'input
    match lancio_moneta:
        case "t":
            t += 1  # incremento per testa
        case "c":
            c += 1  # incremento per croce
        case _:
            print("Lancio non valido. Devi inserire 't' per testa o 'c' per croce.")

# Calcola il numero totale di lanci
i = t + c

# Calcola le percentuali
if i > 0:  # Evita la divisione per zero nel caso non siano stati effettuati lanci validi
    percentuale_testa = (t / i) * 100
    percentuale_croce = (c / i) * 100
    print(f"\nNumero totale di lanci: {i}")
    print(f"Numero di teste: {t} ({percentuale_testa:.2f}%)")
    print(f"Numero di croci: {c} ({percentuale_croce:.2f}%)")
else:
    print("Non sono stati effettuati lanci validi.")




'''
Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età di un utente in un dizionario.
 Il nome, il ruolo e l'età devono essere inseriti in input dall'utente stesso. 
 Il programma deve determinare il livello di accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:

- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"
'''
nome = input("inserisci il nome: ")
ruolo = input("inserisci il ruolo: ")
eta = input("inserisci l'età: ")
Utente={"nome" : nome ,
       "ruolo" : ruolo,
       "eta" : eta}
match Utente:
    case Utente if Utente[ruolo] == "Admin":
        print("Accesso completo a tutte le funzionalità.")
    case Utente if Utente[ruolo] == "Moderatore":
        print("Può gestire i contenuti ma non modificare le impostazioni.")
    case Utente if Utente[eta] >= 18:
        print("Accesso standard a tutti i servizi.")
    case Utente if Utente[eta] <= 18:
        print("Accesso limitato! Alcune funzionalità sono bloccate.")
    case Utente if Utente[ruolo] == "Ospite":
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")
    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")
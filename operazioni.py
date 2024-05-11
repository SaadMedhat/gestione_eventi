import sqlite3

conn = sqlite3.connect("eventi_demo.db")

cursor = conn.cursor()

# cursor.execute(
#     """
#         INSERT INTO Evento(ID, Organizzatore, Nome, Descrizione, Budget, Data, Ora)
#         VALUES (0001, "Alessandro Neri", "Chess Openings", "Evento per gli appassionato del gioco degli scacchi", 5000, 15/05/2024, "10:00:00");
#     """
# )

# cursor.execute(
#     """
#         INSERT INTO Attivita(ID, Descrizione, Durata, OraInizio, idEvento)
#         VALUES (0001, "Questa attivita prevede una presentazione a tutto tondo sugli scacchi, tenuta dal campione del mondo Magnus Carlsen", 00:60, 15:30, 0001);
#     """
# )

# cursor.execute(
#     """
#         INSERT INTO Relatore(Email, Nome, Cognome, Cellulare, Competenza)
#         VALUES (magnus.carles@gmail.com, Magnus, Carlsen, 3271866746, Campione di scacchi);
#     """
# )


queries = [
    """
    SELECT Evento.*
    FROM Evento
    WHERE Evento.Data = "2024-06-15"
    """,
    """
    SELECT E.Nome, SUM(Importo) as "Contributo Totale"
    FROM Evento as E JOIN Finanziamento as F ON E.ID = F.IdEvento
    WHERE E.ID = 2
    """,
    """
    SELECT A.Descrizione
    FROM Evento as E JOIN Attivita as A ON E.ID = A.IdEvento
    WHERE E.ID = 3 AND A.Ora_inizio >= "10:00:00"
    """,
    """
    SELECT *
    FROM Relatore
    WHERE Competenza LIKE "%Developer%"
    """,
    """
    SELECT E.Nome, F.Commento
    FROM Evento as E JOIN Feedback as F ON F.IdEvento = E.ID
    WHERE E.ID = 4
    """,
    """
    SELECT A.ID, A.Descrizione, A.Ora_inizio, A.Durata
    FROM Evento as E JOIN Attivita as A ON E.ID = A.IdEvento
    WHERE E.ID = 3
    """,
    """
    SELECT E.Nome, A.ID, A.Descrizione, A.Ora_inizio, A.Durata
    FROM Evento as E JOIN Attivita as A ON E.ID = A.IdEvento JOIN Intervento as I ON A.ID = I.IdAttivita
    WHERE E.ID = 3
    GROUP BY A.ID
    HAVING COUNT(I.EmailRelatore) >= 1
    """,
    """
    SELECT count(*) as "Numero Partecipanti"
    FROM Evento as E JOIN Iscrizione as I ON E.ID = I.IdEvento
    WHERE E.ID = 1
    """,
    """
    SELECT SUM(T.Ammontare) as "Spesa Totale"
    FROM Evento as E JOIN Transazione as T ON E.ID = T.IdEvento
    WHERE E.ID = 4
    """,
    """
    SELECT AVG(F.Valutazione) as "Valutazione Media"
    FROM Evento as E JOIN Feedback as F ON F.IdEvento = E.ID
    WHERE E.ID = 4
    """,
    """
    SELECT E.Budget + SUM(F.Importo) - L.Costo - SUM(T.Ammontare) as Bilancio
    FROM Evento as E 
    JOIN Finanziamento as F ON E.ID = F.IdEvento 
    JOIN Luogo as L ON E.LuogoIndirizzo = L.Indirizzo
    JOIN Transazione as T ON T.IdEvento = E.ID
    WHERE E.ID = 1
    """,
]


conn.commit()


for idx, query in enumerate(queries):
    print(f"\nQuery {idx+1}:\n{query}\n")
    cursor.execute(query)
    rows = cursor.fetchall()

    # Print column names
    column_names = [description[0] for description in cursor.description]
    print(" | ".join(column_names))

    # Print results
    for row in rows:
        print(" | ".join(map(str, row)))


conn.close()

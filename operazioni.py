import sqlite3

conn = sqlite3.connect("eventi_demo.db")

cursor = conn.cursor()

# cursor.execute(
#     """
#         SELECT Evento.ID
#         FROM Evento
#         WHERE Evento.Data = "15/05/2024"
#     """
# )

# cursor.execute(
#     """
#         SELECT F.EmailSponsor, SUM(Importo)
#         FROM Evento as E JOIN Finanziamento as F ON E.ID = F.IdEvento
#         WHERE E.Nome = "Conference on AI"
#         GROUP BY F.EmailSponsor
#     """
# )

# # query sbagliata
# # cursore.execute(
# #     """
# #         SELECT A.Descrizione
# #         FROM Evento as E JOIN Attivita as A ON Evento.ID = A.idEvento
# #         WHERE Evento.Nome = "Conference on AI    """
# # )

# cursor.execute(
#     """
#         SELECT Nome, Cognome, Cellulare, Email
#         FROM Relatore
#         WHERE Competenza = "Full Stack Developer"
#     """
# )

# cursor.execute(
#     """
#         SELECT F.Commento 
#         FROM Evento as E JOIN Feedback as F ON F.IdEvento = E.ID
#         WHERE E.Nome = "Conference on AI"
#     """
# )

# cursor.execute(
#     """
#         SELECT A.*
#         FROM Evento as E JOIN Attivita as A ON E.ID = A.IdEvento
#     """
# )

# cursor.execute(
#     """
#         SELECT A.ID, A.Descrizione, A.Durata,   
#         A.Ora_inizio
#         FROM Attivita A JOIN Intervento I ON A.ID = I.IdAttivita
#         WHERE A.IdEvento = "1"
#         GROUP BY A.ID
#         HAVING COUNT(I.EmailRelatore) >= 1;
#     """
# )

# cursor.execute(
#     """
#         SELECT count(*) as NumeroPartecipanti
#         FROM Evento as E JOIN Iscrizione as I ON E.ID = I.IdEvento
#         WHERE E.Nome = "Conference on AI"
#     """
# )

# cursor.execute(
#     """
#         SELECT AVG(F.Valutazione) as ValutazioneMedia
#         FROM Evento as E JOIN Feedback as F ON F.IdEvento = E.ID
#         WHERE E.Nome = "Conference on AI"
#     """
# )

# cursor.execute(
#     """
#         SELECT AVG(F.Valutazione)
#         FROM Evento as E JOIN Feedback as F ON F.IdEvento = E.ID
#         WHERE E.Nome = "Conference on AI"
#     """
# )

# cursor.execute(
#     """
#         SELECT E.Budget + SUM(F.Importo) - L.Costo - SUM(T.Ammontare) as Bilancio
#         FROM Evento as E 
#         JOIN Finanziamento as F ON E.ID = F.IdEvento 
#         JOIN Luogo as L ON E.LuogoIndirizzo = L.Indirizzo
#         JOIN Transazione as T ON T.IdEvento = E.ID
#         WHERE E.Nome = "Conference on AI"
#     """
# )

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

# conn.commit()


# risultati = cursor.fetchall()
# for persona in risultati:
#     print(persona)

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
    SELECT A.*
    FROM Evento as E JOIN Attivita as A ON E.ID = A.IdEvento
    """,
    """
    SELECT A.ID, A.Descrizione, A.Durata, A.Ora_inizio
    FROM Attivita A JOIN Intervento I ON A.ID = I.IdAttivita
    WHERE A.IdEvento = "1"
    GROUP BY A.ID
    HAVING COUNT(I.EmailRelatore) >= 1
    """,
    """
    SELECT count(*) as NumeroPartecipanti
    FROM Evento as E JOIN Iscrizione as I ON E.ID = I.IdEvento
    WHERE E.Nome = "Conference on AI"
    """,
    """
    SELECT AVG(F.Valutazione) as ValutazioneMedia
    FROM Evento as E JOIN Feedback as F ON F.IdEvento = E.ID
    WHERE E.Nome = "Conference on AI"
    """,
    """
    SELECT AVG(F.Valutazione)
    FROM Evento as E JOIN Feedback as F ON F.IdEvento = E.ID
    WHERE E.Nome = "Conference on AI"
    """,
    """
    SELECT E.Budget + SUM(F.Importo) - L.Costo - SUM(T.Ammontare) as Bilancio
    FROM Evento as E 
    JOIN Finanziamento as F ON E.ID = F.IdEvento 
    JOIN Luogo as L ON E.LuogoIndirizzo = L.Indirizzo
    JOIN Transazione as T ON T.IdEvento = E.ID
    WHERE E.Nome = "Conference on AI"
    """,
]

# Execute queries and print results
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

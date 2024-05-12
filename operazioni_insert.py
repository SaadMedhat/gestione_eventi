import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("eventi_demo.db")
cursor = conn.cursor()


cursor.execute(
    """
        INSERT INTO Evento(ID, Organizzatore, Nome, Descrizione, Budget, Data, Ora, LuogoIndirizzo)
        VALUES (10, "Alessandro Neri", "Chess Openings", "Evento per gli appassionato del gioco degli scacchi", 5000, "15/05/2024", "10:00:00", "321 Pine Street");
    """
)
conn.commit()
cursor.execute("SELECT * FROM Evento WHERE ID = 10")
print("Operazione 12")
print(cursor.fetchone())

cursor.execute(
    """
        INSERT INTO Attivita(ID, Descrizione, Durata, Ora_inizio, IdEvento)
        VALUES (13, "Questa attivita prevede una presentazione a tutto tondo sugli scacchi, tenuta dal campione del mondo Magnus Carlsen", "00:60", "15:30", 10);
    """
)
conn.commit()
cursor.execute("SELECT * FROM Attivita WHERE ID = 13")
print("Operazione 13")
print(cursor.fetchone())

cursor.execute(
    """
        INSERT INTO Relatore(Email, Nome, Cognome, Cellulare, Competenza)
        VALUES ("magnus.carlsen@gmail.com", "Magnus", "Carlsen", 3271866746, "Campione di scacchi");
    """
)
conn.commit()
cursor.execute("SELECT * FROM Relatore WHERE Email = 'magnus.carlsen@gmail.com'")
print("Operazione 14")
print(cursor.fetchone())

cursor.execute(
    """
        INSERT INTO Intervento(EmailRelatore, IdAttivita) 
        VALUES ("magnus.carlsen@gmail.com", 13);
    """
)
conn.commit()
cursor.execute("SELECT * FROM Intervento WHERE EmailRelatore = 'magnus.carlsen@gmail.com' AND IdAttivita = 13")
print("Operazione 15")
print(cursor.fetchone())

cursor.execute(
    """
        INSERT INTO Partecipante(Email, Nome, Cognome, Cellulare) 
        VALUES ("saad2001f@gmail.com", "Saad Farqad", "Medhat", 3519479169);
    """
)
conn.commit()
cursor.execute("SELECT * FROM Partecipante WHERE Email = 'saad2001f@gmail.com'")
print("Operazione 16")
print(cursor.fetchone())

cursor.execute(
    """
        INSERT INTO Finanziamento(EmailSponsor, IdEvento, Importo) 
        VALUES ("ufficiorelazioniesterne@barilla.it", 10, 2000);
    """
)
conn.commit()
cursor.execute("SELECT * FROM Finanziamento WHERE EmailSponsor = 'ufficiorelazioniesterne@barilla.it' AND IdEvento = 10")
print("Operazione 17")
print(cursor.fetchone())

conn.close()

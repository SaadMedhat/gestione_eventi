import sqlite3

conn = sqlite3.connect("eventi_demo.db")

cursor = conn.cursor()

# Create tables
cursor.execute(
    """
    CREATE TABLE Evento (
        ID INTEGER PRIMARY KEY,
        Organizzatore VARCHAR(64),
        Nome VARCHAR(64),
        Descrizione VARCHAR(255),
        Budget DECIMAL,
        Data DATE,
        Ora TIME,
        LuogoIndirizzo VARCHAR(128),
        FOREIGN KEY (LuogoIndirizzo) REFERENCES Luogo(Indirizzo)
    )"""
)

cursor.execute(
    """
    CREATE TABLE Attivita (
        ID INTEGER PRIMARY KEY,
        Descrizione VARCHAR(255),
        Durata TIME,
        Ora_inizio TIME,
        IdEvento INTEGER,
        FOREIGN KEY (IdEvento) REFERENCES Evento(ID)
    )"""
)

cursor.execute(
    """
    CREATE TABLE Relatore (
        Email VARCHAR(128) PRIMARY KEY,
        Nome VARCHAR(64),
        Cognome VARCHAR(64),
        Cellulare VARCHAR(10),
        Competenza VARCHAR(64)
    )"""
)

cursor.execute(
    """
    CREATE TABLE Sponsor (
        Email VARCHAR(128) PRIMARY KEY,
        Nome VARCHAR(64),
        Cellulare VARCHAR(10)
    )"""
)

cursor.execute(
    """
    CREATE TABLE Partecipante (
        Email VARCHAR(128) PRIMARY KEY,
        Nome VARCHAR(64),
        Cognome VARCHAR(64),
        Cellulare VARCHAR(10)
    )"""
)

cursor.execute(
    """
    CREATE TABLE Luogo (
        Indirizzo VARCHAR(128) PRIMARY KEY,
        Capacita INTEGER,
        Costo DECIMAL
    )"""
)

cursor.execute(
    """
    CREATE TABLE Pubblicita (
        ID INTEGER PRIMARY KEY,
        Visualizzazioni INTEGER,
        Canale VARCHAR(32),
        IdEvento INTEGER,
        FOREIGN KEY (IdEvento) REFERENCES Evento(ID)
    )"""
)

cursor.execute(
    """
    CREATE TABLE Transazione (
        ID INTEGER PRIMARY KEY,
        Descrizione VARCHAR(255),
        Data DATE,
        Ammontare DECIMAL,
        IdEvento INTEGER,
        FOREIGN KEY (IdEvento) REFERENCES Evento(ID)
    )"""
)

cursor.execute(
    """
    CREATE TABLE Intervento (
        EmailRelatore VARCHAR(64),
        IdAttivita INTEGER,
        PRIMARY KEY (EmailRelatore, IdAttivita),
        FOREIGN KEY (EmailRelatore) REFERENCES Relatore(Email),
        FOREIGN KEY (IdAttivita) REFERENCES Attivita(ID)
    )"""
)

cursor.execute(
    """
    CREATE TABLE Finanziamento (
        EmailSponsor VARCHAR(128),
        IdEvento INTEGER,
        Importo DECIMAL,
        PRIMARY KEY (EmailSponsor, IdEvento),
        FOREIGN KEY (EmailSponsor) REFERENCES Sponsor(Email),
        FOREIGN KEY (IdEvento) REFERENCES Evento(ID)
    )"""
)

cursor.execute(
    """
    CREATE TABLE Feedback (
        EmailPartecipante VARCHAR(128),
        IdEvento INTEGER,
        Valutazione INTEGER,
        Commento VARCHAR(255),
        PRIMARY KEY (EmailPartecipante, IdEvento),
        FOREIGN KEY (EmailPartecipante) REFERENCES Partecipante(Email),
        FOREIGN KEY (IdEvento) REFERENCES Evento(ID)
    )"""
)

cursor.execute(
    """
    CREATE TABLE Iscrizione (
        EmailPartecipante VARCHAR(128),
        IdEvento INTEGER,
        Costo_del_biglietto DECIMAL,
        Data_di_iscrizione DATE,
        PRIMARY KEY (EmailPartecipante, IdEvento),
        FOREIGN KEY (EmailPartecipante) REFERENCES Partecipante(Email),
        FOREIGN KEY (IdEvento) REFERENCES Evento(ID)
    )"""
)

conn.commit()
conn.close()

import sqlite3

conn = sqlite3.connect("eventi_demo.db")

cursor = conn.cursor()

cursor.execute(
    """
      CREATE TABLE Evento (
        ID int PRIMARY KEY,
        Organizzatore varchar(64),
        Nome varchar(64),
        Descrizione varchar(255),
        Budget DECIMAL CHECK (Budget >= 0),
        Data DATE,
        Ora TIME,
        Costo_del_biglietto DECIMAL CHECK(Costo_del_biglietto > 0),
        LuogoIndirizzo Indirizzo,
        FOREIGN KEY (LuogoIndirizzo) REFERENCES Luogo(Indirizzo)
    )
    """
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
    )
    """
)

cursor.execute(
    """
    CREATE TABLE Relatore (
        Email VARCHAR(128) PRIMARY KEY,
        Nome VARCHAR(64),
        Cognome VARCHAR(64),
        Cellulare VARCHAR(10),
        Competenza VARCHAR(64)
    )
    """
)

cursor.execute(
    """
    CREATE TABLE Sponsor (
        Email VARCHAR(128) PRIMARY KEY,
        Nome VARCHAR(64),
        Cellulare VARCHAR(10)
    )
    """
)

cursor.execute(
    """
    CREATE TABLE Partecipante (
        Email VARCHAR(128) PRIMARY KEY,
        Nome VARCHAR(64),
        Cognome VARCHAR(64),
        Cellulare VARCHAR(10)
    )
    """
)

cursor.execute(
    """
    CREATE TABLE Luogo (
        Indirizzo varchar(128) PRIMARY KEY,
        Capacita int,
        Costo DECIMAL CHECK (Costo >= 0)
    )
    """
)

cursor.execute(
    """
    CREATE TABLE Pubblicita (
        ID int PRIMARY KEY,
        Visualizzazioni int CHECK (Visualizzazioni >= 0),
        Canale varchar(32) CHECK (Canale IN ('Facebook', 'Instagram', 'X', 'Threads')),
        IdEvento int,
        FOREIGN KEY (IdEvento) REFERENCES Evento(ID)
    )
    """
)

cursor.execute(
    """
    CREATE TABLE Transazione (
        ID int PRIMARY KEY,
        Descrizione varchar(255),
        Data DATE,
        Ammontare DECIMAL CHECK(Ammontare >= 0),
        IdEvento int,
        FOREIGN KEY (IdEvento) REFERENCES Evento(ID)
    )
    """
)

cursor.execute(
    """
    CREATE TABLE Intervento (
        EmailRelatore VARCHAR(64),
        IdAttivita INTEGER,
        PRIMARY KEY (EmailRelatore, IdAttivita),
        FOREIGN KEY (EmailRelatore) REFERENCES Relatore(Email),
        FOREIGN KEY (IdAttivita) REFERENCES Attivita(ID)
    )
    """
)

cursor.execute(
    """
    CREATE TABLE Finanziamento (
        EmailSponsor varchar(128),
        IdEvento int,
        Importo DECIMAL CHECK (Importo >= 0),
        PRIMARY KEY (EmailSponsor, IdEvento),
        FOREIGN KEY (EmailSponsor) REFERENCES Sponsor(Email),
        FOREIGN KEY (IdEvento) REFERENCES Evento(ID)
    )
    """
)

cursor.execute(
    """
    CREATE TABLE Feedback (
        EmailPartecipante varchar(128),
        IdEvento INTEGER,
        Valutazione INTEGER CHECK (Valutazione >= 1 and Valutazione <= 10),
        Commento varchar(255),
        PRIMARY KEY (EmailPartecipante, IdEvento),
        FOREIGN KEY (EmailPartecipante) REFERENCES Partecipante(Email),
        FOREIGN KEY (IdEvento) REFERENCES Evento(ID)
    )
    """
)

cursor.execute(
    """
    CREATE TABLE Iscrizione (
        EmailPartecipante VARCHAR(128),
        IdEvento INTEGER,
        Data_di_iscrizione DATE,
        PRIMARY KEY (EmailPartecipante, IdEvento),
        FOREIGN KEY (EmailPartecipante) REFERENCES Partecipante(Email),
        FOREIGN KEY (IdEvento) REFERENCES Evento(ID)
    )
    """
)

conn.commit()
conn.close()

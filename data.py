import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("eventi_demo.db")
cursor = conn.cursor()

# Sample data for tables
eventi_data = [
    (
        1,
        "John Doe",
        "Conference on AI",
        "A conference discussing the latest advancements in Artificial Intelligence.",
        5000.00,
        "2024-06-15",
        "09:00:00",
        "123 Main Street",
    ),
    (
        2,
        "Jane Smith",
        "Workshop on Python Programming",
        "A workshop for beginners to learn Python programming language.",
        3000.00,
        "2024-07-20",
        "13:30:00",
        "456 Elm Street",
    ),
    (
        3,
        "Michael Johnson",
        "Web Development Bootcamp",
        "A bootcamp for mastering web development technologies.",
        7000.00,
        "2024-08-10",
        "10:00:00",
        "789 Oak Avenue",
    ),
    (
        4,
        "Emma Watson",
        "Seminar on Data Science",
        "A seminar discussing the applications of Data Science.",
        4000.00,
        "2024-09-15",
        "10:00:00",
        "321 Pine Street",
    ),
    (
        5,
        "Robert Smith",
        "Workshop on Cybersecurity",
        "A workshop for understanding the basics of Cybersecurity.",
        3500.00,
        "2024-10-20",
        "14:00:00",
        "654 Willow Street",
    ),
    (
        6,
        "Sophia Johnson",
        "Cloud Computing Bootcamp",
        "A bootcamp for learning about Cloud Computing technologies.",
        6000.00,
        "2024-11-10",
        "11:00:00",
        "987 Maple Avenue",
    ),
    (
        7,
        "Olivia Williams",
        "Conference on Blockchain",
        "A conference discussing the latest advancements in Blockchain technology.",
        4500.00,
        "2024-12-15",
        "09:30:00",
        "159 Cedar Street",
    ),
    (
        8,
        "James Brown",
        "Workshop on Quantum Computing",
        "A workshop for beginners to learn Quantum Computing.",
        3200.00,
        "2025-01-20",
        "13:00:00",
        "753 Spruce Street",
    ),
    (
        9,
        "Emily Davis",
        "Artificial Intelligence Bootcamp",
        "A bootcamp for mastering AI technologies.",
        6500.00,
        "2025-02-10",
        "10:30:00",
        "369 Birch Avenue",
    ),
]

attivita_data = [
    (1, "Introduction to Machine Learning", "01:30:00", "09:00:00", 1),
    (2, "Hands-on Python Coding", "02:00:00", "14:30:00", 2),
    (3, "HTML & CSS Basics", "01:30:00", "10:00:00", 3),
    (4, "JavaScript Fundamentals", "02:00:00", "14:00:00", 3),
    (5, "Data Science Concepts", "01:30:00", "10:00:00", 4),
    (6, "Cybersecurity Essentials", "02:00:00", "15:00:00", 5),
    (7, "Cloud Computing Basics", "01:30:00", "11:00:00", 6),
    (8, "Advanced Cloud Technologies", "02:00:00", "15:00:00", 6),
    (9, "Blockchain Concepts", "01:30:00", "09:30:00", 7),
    (10, "Quantum Computing Essentials", "02:00:00", "14:00:00", 8),
    (11, "AI Basics", "01:30:00", "10:30:00", 9),
    (12, "Advanced AI Technologies", "02:00:00", "15:00:00", 9),
]

relatore_data = [
    ("johndoe@example.com", "John", "Doe", "1234567890", "Machine Learning Expert"),
    ("janesmith@example.com", "Jane", "Smith", "0987654321", "Python Developer"),
    (
        "michaeljohnson@example.com",
        "Michael",
        "Johnson",
        "9876543210",
        "Full Stack Developer",
    ),
    ("emmawatson@example.com", "Emma", "Watson", "1234567891", "Data Science Expert"),
    (
        "robertsmith@example.com",
        "Robert",
        "Smith",
        "0987654322",
        "Cybersecurity Specialist",
    ),
    (
        "sophiajohnson@example.com",
        "Sophia",
        "Johnson",
        "9876543211",
        "Cloud Computing Expert",
    ),
    (
        "oliviawilliams@example.com",
        "Olivia",
        "Williams",
        "1234567892",
        "Blockchain Expert",
    ),
    (
        "jamesbrown@example.com",
        "James",
        "Brown",
        "0987654323",
        "Quantum Computing Specialist",
    ),
    (
        "emilydavis@example.com",
        "Emily",
        "Davis",
        "9876543212",
        "AI Expert",
    ),
]

sponsor_data = [
    ("sponsor1@example.com", "TechCorp", "1234567890"),
    ("sponsor2@example.com", "CodeMaster", "0987654321"),
    ("sponsor3@example.com", "WebTech", "9876543210"),
    ("sponsor4@example.com", "DataCorp", "1234567891"),
    ("sponsor5@example.com", "SecureMaster", "0987654322"),
    ("sponsor6@example.com", "CloudTech", "9876543211"),
    ("sponsor7@example.com", "BlockCorp", "1234567892"),
    ("sponsor8@example.com", "QuantumMaster", "0987654323"),
    ("sponsor9@example.com", "AITech", "9876543212"),
]

partecipante_data = [
    ("participant1@example.com", "Alice", "Johnson", "3648458763"),
    ("participant2@example.com", "Bob", "Williams", "3278566943"),
    ("participant3@example.com", "Charlie", "Brown", "3852734532"),
    ("participant4@example.com", "David", "Miller", "3648458764"),
    ("participant5@example.com", "Eva", "Martinez", "3278566944"),
    ("participant6@example.com", "Frank", "Garcia", "3852734533"),
    ("participant7@example.com", "George", "Taylor", "3648458765"),
    ("participant8@example.com", "Chloe", "Anderson", "3278566945"),
    ("participant9@example.com", "Daniel", "Thomas", "3852734534"),
]

luogo_data = [
    ("123 Main Street", 200, 1000.00),
    ("456 Elm Street", 150, 800.00),
    ("789 Oak Avenue", 300, 1200.00),
    ("321 Pine Street", 250, 1100.00),
    ("654 Willow Street", 200, 900.00),
    ("987 Maple Avenue", 350, 1300.00),
    ("159 Cedar Street", 275, 1150.00),
    ("753 Spruce Street", 225, 950.00),
    ("369 Birch Avenue", 375, 1350.00),
]


pubblicita_data = [
    (1, 10000, "Facebook", 1),
    (2, 8000, "Instagram", 2),
    (3, 5000, "Threads", 3),
]

transazione_data = [
    (1, "Ticket sales", "2024-06-01", 2000.00, 1),
    (2, "Workshop fees", "2024-07-10", 1500.00, 2),
    (3, "Bootcamp registration", "2024-08-01", 3000.00, 3),
    (4, "Seminar fees", "2024-09-01", 1800.00, 4),
    (5, "Workshop fees", "2024-10-10", 1750.00, 5),
    (6, "Bootcamp registration", "2024-11-01", 2500.00, 6),
    (7, "Conference fees", "2024-12-01", 2250.00, 7),
    (8, "Workshop fees", "2025-01-10", 1600.00, 8),
    (9, "Bootcamp registration", "2025-02-01", 3250.00, 9),
]

intervento_data = [
    ("johndoe@example.com", 1),
    ("janesmith@example.com", 2),
    # ("michaeljohnson@example.com", 3),
    ("emmawatson@example.com", 4),
    ("robertsmith@example.com", 5),
    ("sophiajohnson@example.com", 6),
    ("oliviawilliams@example.com", 7),
    ("jamesbrown@example.com", 8),
    ("emilydavis@example.com", 9),
]

finanziamento_data = [
    ("sponsor1@example.com", 1, 2000.00),
    ("sponsor4@example.com", 2, 500.00),
    ("sponsor2@example.com", 2, 1500.00),
    ("sponsor3@example.com", 3, 3000.00),
    ("sponsor4@example.com", 4, 1800.00),
    ("sponsor5@example.com", 5, 1750.00),
    ("sponsor6@example.com", 6, 2500.00),
    ("sponsor7@example.com", 7, 2250.00),
    ("sponsor8@example.com", 8, 1600.00),
    ("sponsor9@example.com", 9, 3250.00),
]

feedback_data = [
    ("participant1@example.com", 1, 10, "Great conference!"),
    ("participant2@example.com", 2, 8, "Enjoyed the workshop."),
    ("participant3@example.com", 3, 8, "Very informative bootcamp."),
    ("participant4@example.com", 4, 10, "Informative seminar!"),
    ("participant2@example.com", 4, 7, "Very useful seminar"),
    ("participant5@example.com", 5, 8, "Loved the workshop."),
    ("participant6@example.com", 6, 8, "Great bootcamp."),
    ("participant7@example.com", 7, 10, "Excellent conference!"),
    ("participant8@example.com", 8, 8, "Very useful workshop."),
    ("participant9@example.com", 9, 8, "Informative bootcamp."),
]

iscrizione_data = [
    ("participant1@example.com", 1, 50.00, "2024-05-15"),
    ("participant2@example.com", 1, 50.00, "2024-05-15"),
    ("participant3@example.com", 1, 50.00, "2024-05-15"),
    ("participant2@example.com", 2, 30.00, "2024-07-01"),
    ("participant5@example.com", 2, 30.00, "2024-07-01"),
    ("participant6@example.com", 2, 30.00, "2024-07-01"),
    ("participant3@example.com", 3, 70.00, "2024-07-25"),
    ("participant4@example.com", 4, 40.00, "2024-08-15"),
    ("participant5@example.com", 5, 35.00, "2024-10-01"),
    ("participant6@example.com", 6, 60.00, "2024-10-25"),
    ("participant7@example.com", 7, 45.00, "2024-11-15"),
    ("participant8@example.com", 8, 32.00, "2025-01-01"),
    ("participant9@example.com", 9, 65.00, "2025-01-25"),
]

# Commented code
cursor.executemany("INSERT INTO Evento VALUES (?, ?, ?, ?, ?, ?, ?, ?)", eventi_data)
cursor.executemany("INSERT INTO Attivita VALUES (?, ?, ?, ?, ?)", attivita_data)
cursor.executemany("INSERT INTO Relatore VALUES (?, ?, ?, ?, ?)", relatore_data)
cursor.executemany("INSERT INTO Sponsor VALUES (?, ?, ?)", sponsor_data)
cursor.executemany("INSERT INTO Partecipante VALUES (?, ?, ?, ?)", partecipante_data)
cursor.executemany("INSERT INTO Luogo VALUES (?, ?, ?)", luogo_data)
cursor.executemany("INSERT INTO Pubblicita VALUES (?, ?, ?, ?)", pubblicita_data)
cursor.executemany("INSERT INTO Transazione VALUES (?, ?, ?, ?, ?)", transazione_data)
cursor.executemany("INSERT INTO Intervento VALUES (?, ?)", intervento_data)
cursor.executemany("INSERT INTO Finanziamento VALUES (?, ?, ?)", finanziamento_data)
cursor.executemany("INSERT INTO Feedback VALUES (?, ?, ?, ?)", feedback_data)
cursor.executemany("INSERT INTO Iscrizione VALUES (?, ?, ?, ?)", iscrizione_data)

conn.commit()

risultati = cursor.fetchall()
for persona in risultati:
    print(persona)

conn.close()

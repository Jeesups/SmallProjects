import sqlite3
connection = sqlite3.connect("test.db")

#Dostep do kolumn przez indesky i przez nazwy
connection.row_factory = sqlite3.Row

#utworzenie obiektu kursora
currsor = connection.cursor()


currsor.execute("DROP TABLE IF EXISTS klasa;")

currsor.execute("""CREATE TABLE IF NOT EXISTS klasa(
    id INTEGER PRIMARY KEY ASC,
    nazwa VARCHAR(250) NOT NULL,
    profil VARCHAR(250) DEFAULT ''
);""")
'''
    execute - pozwala ruszyc pojedynczy skrypt
    executescript - pozwala wykonywac kilka procedur
'''


currsor.executescript("""DROP TABLE IF EXISTS uczen;
CREATE TABLE IF NOT EXISTS  uczen(
    id INTEGER PRIMARY KEY ASC,
    imie VARCHAR(250) NOT NULL,
    nazwisko VARCHAR(250) NOT NULL,
    klasa_id INTEGER NOT NULL,
    FOREIGN KEY(klasa_id) REFERENCES klasa(id)
); """)


#Wstawianie danych


currsor.execute('INSERT INTO klasa VALUES(NULL,?,?);',('1A','matematyczny'))
currsor.execute('INSERT INTO klasa VALUES(NULL,?,?);',('1B','humanistyczny'))

#Zapytanie pobrania id 
currsor.execute('SELECT id FROM klasa WHERE nazwa = ?',('1A',))
klasa_id = currsor.fetchone()[0]
#tuplaczu uczniowie

uczniowie = (
    (None,'Tomasz','Nowak',klasa_id),
    (None,'Jan','Kos',klasa_id),
    (None,'Piotr','Kowalski',klasa_id)
)

#Wstawiamy wiele rekordow
currsor.executemany('INSERT INTO uczen VALUES (?,?,?,?)',uczniowie)

#zatwierdzamy zmiany w bazie danych
connection.commit()
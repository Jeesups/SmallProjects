import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

def czytajDane():
    '''Funkcja pobiera i wyswietla dane z bazy.cursor'''
    
    cursor.execute("""
        SELECT uczen.id,imie,nazwisko,nazwa FROM uczen,klasa
        WHERE uczen.klasa_id = klasa.id
    """)
    uczniowie = cursor.fetchall()
    for uczen in uczniowie:
       print("{}, {} , {}, {}".format(uczen[0],uczen[1], uczen[2],uczen[3]))        
    print()

czytajDane()

cursor.execute("SELECT id FROM klasa WHERE nazwa = {}".format('18'))
klasa_id = cursor.fetchone()[0]
cursor.execute('UPDATE uczen SET klasa_id = {} WHERE id = {}'.format(klasa_id,2))
cursor.execute("DELETE FROM uczen WHERE id = {}".format(3))

czytajDane()
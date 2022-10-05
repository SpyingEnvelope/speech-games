import sqlite3

conn = sqlite3.connect('words-database.db')

c = conn.cursor()

c.execute("""
    CREATE TABLE e_initial (
        word text,
        path text
    )
    """)

print('Table successfully created')

# conn.commit()

many_words = [
    ('Eagle', 'words_database/e-initial/eagle.png'),
    ('Ear', 'words_database/e-initial/ear.png'),
    ('Earth', 'words_database/e-initial/earth.png'),
    ('Echidna', 'words_database/e-initial/echidna.png'),
    ('Echo', 'words_database/e-initial/echo.png'),
    ('Egg', 'words_database/e-initial/egg.png'),
    ('Eggplant', 'words_database/e-initial/eggplant.png'),
    ('Eight', 'words_database/e-initial/eight.png'),
    ('Elephant', 'words_database/e-initial/elephant.png'),
    ('Elevator', 'words_database/e-initial/elevator.png'),
    ('Eleven', 'words_database/e-initial/eleven.png'),
    ('Elk', 'words_database/e-initial/elk.png'),
    ('End', 'words_database/e-initial/end.png'),
    ('Eraser', 'words_database/e-initial/eraser.png'),
    ('Exit', 'words_database/e-initial/exit.png')
]

c.executemany("INSERT INTO e_initial VALUES (?,?)", many_words)
print('words and paths successfully added to database')

conn.commit()
print('finished commiting changes')
conn.close()
print('closing connection')
import sqlite3

conn = sqlite3.connect('words-database.db')

c = conn.cursor()

c.execute("""
    CREATE TABLE a_initial (
        word text,
        path text
    )
    """)

print('Table successfully created')

# conn.commit()

many_words = [
    ('Acorn', 'words_database/a-initial/acorn.png'),
    ('Alligator', 'words_database/a-initial/alligator.png'),
    ('Angel', 'words_database/a-initial/angel.png'),
    ('Antlers', 'words_database/a-initial/antlers.png'),
    ('Arrow', 'words_database/a-initial/arrow.png'),
    ('Adult', 'words_database/a-initial/adult.png'),
    ('Alphabet', 'words_database/a-initial/alphabet.png'),
    ('Angry', 'words_database/a-initial/angry.png'),
    ('Ape', 'words_database/a-initial/ape.png'),
    ('Astronaut', 'words_database/a-initial/astronaut.png'),
    ('Airplane', 'words_database/a-initial/airplane.png'),
    ('Ambulance', 'words_database/a-initial/ambulance.png'),
    ('Ant', 'words_database/a-initial/ant.png'),
    ('Apple', 'words_database/a-initial/apple.png'),
    ('Axe', 'words_database/a-initial/axe.png')
]

c.executemany("INSERT INTO a_initial VALUES (?,?)", many_words)
print('words and paths successfully added to database')

conn.commit()
print('finishec commiting changes')
conn.close()
print('closing connection')
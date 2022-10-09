import sqlite3

conn = sqlite3.connect('words-database.db')

c = conn.cursor()

c.execute("""
    CREATE TABLE h_initial (
        word text,
        path text
    )
    """)

print('Table successfully created')

# conn.commit()

many_words = [
    ('Hand', 'words_database/h-initial/hand.png'),
    ('Hat', 'words_database/h-initial/hat.png'),
    ('Heart', 'words_database/h-initial/heart.png'),
    ('Hen', 'words_database/h-initial/hen.png'),
    ('Her', 'words_database/h-initial/her.png'),
    ('Hide', 'words_database/h-initial/hide.png'),
    ('Hill', 'words_database/h-initial/hill.png'),
    ('Him', 'words_database/h-initial/him.png'),
    ('Hockey', 'words_database/h-initial/hockey.png'),
    ('Hole', 'words_database/h-initial/hole.png'),
    ('Horse', 'words_database/h-initial/horse.png'),
    ('Hot', 'words_database/h-initial/hot.png'),
    ('House', 'words_database/h-initial/house.png'),
    ('Hug', 'words_database/h-initial/hug.png'),
    ('Hurt', 'words_database/h-initial/hurt.png')
]

c.executemany("INSERT INTO h_initial VALUES (?,?)", many_words)
print('words and paths successfully added to database')

conn.commit()
print('finished commiting changes')
conn.close()
print('closing connection')
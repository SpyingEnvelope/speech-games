import sqlite3

conn = sqlite3.connect('words-database.db')

c = conn.cursor()

c.execute("""
    CREATE TABLE j_initial (
        word text,
        path text
    )
    """)

print('Table successfully created')

# conn.commit()

many_words = [
    ('Jacket', 'words_database/j-initial/jacket.png'),
    ('Jam', 'words_database/j-initial/jam.png'),
    ('Jeans', 'words_database/j-initial/jeans.png'),
    ('Jewel', 'words_database/j-initial/jewel.png'),
    ('Juggling', 'words_database/j-initial/juggling.png'),
    ('Jaguar', 'words_database/j-initial/jaguar.png'),
    ('Janitor', 'words_database/j-initial/janitor.png'),
    ('Jelly Beans', 'words_database/j-initial/jellybeans.png'),
    ('Jingle Bells', 'words_database/j-initial/jinglebells.png'),
    ('Juice', 'words_database/j-initial/juice.png'),
    ('Jail', 'words_database/j-initial/jail.png'),
    ('Jar', 'words_database/j-initial/jar.png'),
    ('Jet', 'words_database/j-initial/jet.png'),
    ('Jog', 'words_database/j-initial/jog.png'),
    ('Jump', 'words_database/j-initial/jump.png')
]

c.executemany("INSERT INTO j_initial VALUES (?,?)", many_words)
print('words and paths successfully added to database')

conn.commit()
print('finished commiting changes')
conn.close()
print('closing connection')
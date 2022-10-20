import os
import sqlite3

### PLEASE ENSURE YOU REMOVE THE TABLES YOU WOULD LIKE TO ADD AND MODIFY dirs_names APPROPRIETLY, OTHERWISE THE SCRIPT WILL CRASH

conn = sqlite3.connect('words-database.db')

c = conn.cursor()

dirs_names = [
    'k-initial', 
    'l-initial', 
    'm-initial', 
    'n-initial', 
    'o-initial', 
    'p-initial', 
    'q-initial', 
    'r-initial', 
    's-initial', 
    't-initial', 
    'u-initial', 
    'v-initial', 
    'w-initial', 
    'x-initial', 
    'y-initial', 
    'z-initial'
    ]

tables_names = [
    'k_initial', 
    'l_initial', 
    'm_initial', 
    'n_initial', 
    'o_initial', 
    'p_initial', 
    'q_initial', 
    'r_initial', 
    's_initial', 
    't_initial', 
    'u_initial', 
    'v_initial', 
    'w_initial', 
    'x_initial', 
    'y_initial', 
    'z_initial'
    ]


for dir_name in dirs_names:
    os.chdir(dir_name)
    dir_name_index = dirs_names.index(dir_name)
    table_name = tables_names[dir_name_index]

    c.execute("CREATE TABLE " + table_name + " (word text, path text)")

    image_names = os.listdir()
    for image in image_names:
        period_index = image.index('.')        
        word = image[:period_index]
        word = word.capitalize()

        path = 'words_database/' + dir_name + '/' + image

        entry = (word, path)

        c.execute("INSERT INTO " + table_name + " VALUES (?,?)", entry)
        conn.commit()

        print(entry[0] + " was committed to database")
    
    os.chdir('..')

import requests
from bs4 import BeautifulSoup
import re
import sqlite3

# def url_input():
#     url = input('Input URL (type exit to quit): ')

#     if url == 'quit':
#         exit()

#     # page = requests.get(url)

#     try:
#         page = requests.get(url)
#     except:
#         print('invalid url, please try again')
#         url_input()

#     soup = BeautifulSoup(page.content, 'html.parser')
#     for line in soup.find_all('a'):
#         line_str = str(line)
#         search_result = re.search('a\shref="a[a-z]{2,5}"', line_str)
#         if search_result:
#             index = line_str.rindex('"')
#             print(line_str[9:index])

# url_input()

abc_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter in abc_list:
    conn = sqlite3.connect('words.db')
    c = conn.cursor()

    c.execute("CREATE TABLE " + letter +  "_initial (word text)")

    url = 'https://www.thefreedictionary.com/words-that-start-with-' + letter

    try:
        page = requests.get(url)
    except:
        print('error. Skipped letter' + letter)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    for line in soup.find_all('a'):
        line_str = str(line)
        search_result = re.search('a\shref="' + letter + '[a-z]{4,5}"', line_str)
        if search_result:
            index = line_str.rindex('"')
            print(line_str[9:index])
            c.execute("INSERT INTO " + letter + "_initial VALUES (?)", (line_str[9:index],))
            print(line_str[9:index] + ' sucessfully entered into database')
            conn.commit()
        
    conn.close()


import sqlite3
import random
conn = sqlite3.connect('listwords.s3db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS words(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               German TEXT,
               Translated TEXT
               );""")

class Words:
    def __init__(self):
        self.count = 0
    def input_words_and_translated(self):
        input_word = input('Enter the German:')
        translated_word = input('Enter the translated:')
        cur.execute("INSERT INTO words (GERMAN, Translated) VALUES (?, ?);", (input_word, translated_word))

class UserInterface:
    words = Words()
    while True:
        print("1. Enter the word and the translated:\n2. Random a words and their translated\n0. Exit Program")
        choice = int(input())
        if choice == 1:
            words.input_words_and_translated()
            conn.commit()
        if choice == 2:
            cur.execute('SELECT COUNT(id) FROM words;')
            count = cur.fetchone()[0]
            cur.execute('SELECT German, Translated FROM words WHERE id = (?);', (str(random.randrange(1,int(count))),))
            print(cur.fetchone())
        if choice == 0:
            exit()







import sqlite3

db = sqlite3.connect('contacts.sqlite')
name = input("Please enter your name: ")

# THIS IS HOW YOU PROVIDE A TUPLE THAT SUPPLIES A SINGLE VALUE *USEFUL*
for row in db.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(row)

db.close()
import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Mitchell', 11234567890, 'mitchdirt@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'Brian@myemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# This fetches all entries and puts them in tuples inside a list.
print(cursor.fetchall())

# This fetches one entry at a time
# This command will print None for all print statements because there are no more entries to grab.
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

# This for loop would unpack the tuples in the contacts table, however; there is nothing left to unpack.
for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print('-' * 40)

# You need to close the cursor since it isn't being used anymore.
cursor.close()

# If you want to save the data to be used elsewhere you need to commit it.
db.commit()

# After committing changes *IF THEY ARE CORRECT* you need to close the database.
db.close()

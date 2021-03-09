import sqlite3

# This variable is used to connect to the contacts database.
db = sqlite3.connect("contacts.sqlite")

new_email = "newemail@update.com"
phone = input("Please enter the phone number: ")

# Update the email of any entries with a phone number equal to `1234`.
# The ? in the string are placeholders. Checks for addition sql statements (good for stopping SQL injection).
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
print(update_sql)

update_cursor = db.cursor()

# `executescript` is used for running multiple statements at the same time.
# If using `executescript` it doesn't set the row count, that is why when making changes it displays negative numbers.
# (new_email, phone) is used to let the update_sql command know what the placeholders(`?`) will be.
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows updated".format(update_cursor.rowcount))

# This shows that update_cursor.connection equals db. You should try and update using connections like this.
print()
print("Are connections the same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()

# Shortcut that can be used instead of the cursor. Cursor is clearer but this is acceptable.
for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print('-' * 30)

db.close()
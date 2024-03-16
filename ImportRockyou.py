import sqlite3

# WARNING: This will take multiple minutes to finish, please use the Passwords.db file or have made or be patient

# Connect to the SQLite database (if it doesn't exist, it will be created)
conn = sqlite3.connect('Passwords.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the table if it doesn't exist already
cursor.execute('''CREATE TABLE IF NOT EXISTS Rockyou (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Password TEXT
                  )''')

# Open the file and read passwords line by line
with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as file:
    passwords = file.readlines()

# Insert each password into the table
for password in passwords:
    
    # Remove newline character from the end of each line
    password = password.strip()
    
    # Insert password into the table
    print("Importing:", password)
    cursor.execute("INSERT INTO Rockyou (Password) VALUES (?)", (password,))

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data inserted successfully.")

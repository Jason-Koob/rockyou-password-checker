import sqlite3

conn = sqlite3.connect('Passwords.db')

cursor = conn.cursor()

def NewPassword(Website, Website_URL, Username, Password):
    try:

        # Create the table if it doesn't exist already
        cursor.execute('''CREATE TABLE IF NOT EXISTS Personal (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Website TEXT,
                            Website_URL TEXT,
                            Username TEXT,
                            Password TEXT,
                            In_Rockyou BOOL
                        )''')

        # Check if the website already exists in the Personal table
        cursor.execute("SELECT * FROM Personal WHERE Website = ?", (Website,))
        existing_row = cursor.fetchone()
        
        if existing_row:

            # Website already exists, update the row with the new username and password
            cursor.execute("UPDATE Personal SET Username = ?, Password = ? WHERE Website = ?",
                           (Username, Password, Website))
            print(f"Username and password for {Website} updated successfully.")
        else:

            # Website does not exist, insert a new row with the provided information
            cursor.execute("INSERT INTO Personal (Website, Website_URL, Username, Password) VALUES (?, ?, ?, ?)",
                           (Website, Website_URL, Username, Password))
            print("New password record added successfully.")
        
        # Commit the transaction
        conn.commit()

        # Script to check if any password from Personal are in Rockyou table
        from CheckPersonal import update_personal_table

    except sqlite3.Error as e:
        print("Error updating or inserting new password:", e)

# Call the Script
UseWebsite = input("What is the Website? (google)\n")
UseURL = input("What is the Website URL? (https://google.com)\n")
UseUsername = input("What is the Username?\n")
UsePassword = input("What is the Password\n")
NewPassword(UseWebsite, UseURL, UseUsername, UsePassword)
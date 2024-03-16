import sqlite3

# Connect to the SQLite database (if it doesn't exist, it will be created)
conn = sqlite3.connect('Passwords.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

print(f"\nChecking if any of your passwords are in rockyou.")

def update_personal_table():
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
        
        # Get all website-password pairs from the Personal table
        cursor.execute("SELECT Website, Password FROM Personal")
        rows = cursor.fetchall()
        
        # Iterate over each website-password pair
        for row in rows:
            website, password = row
            
            # Check if the password exists in the Rockyou table
            cursor.execute("SELECT EXISTS(SELECT 1 FROM Rockyou WHERE Password = ?)", (password,))
            result = cursor.fetchone()[0]
            
            # If password found in Rockyou table, alert the user
            if result:
                print(f"Alert: Password found in Rockyou table for website '{website}' with password '{password}'")
                
            # Update In_Rockyou column accordingly
            cursor.execute("UPDATE Personal SET In_Rockyou = ? WHERE Password = ?", (result, password))
            
            # If password not found in Rockyou table, set In_Rockyou to 0
            if not result:
                cursor.execute("UPDATE Personal SET In_Rockyou = 0 WHERE Password = ?", (password,))

        # Commit the transaction
        conn.commit()
        print("\nPersonal Password table checked successfully.")
                
    except sqlite3.Error as e:
        print("Error updating personal table:", e)

    # Wait for User input
    input("Press Enter to quit . . . ")

update_personal_table()

# rockyou-password-checker
Using SQLite3, I have created a database some of the passwords from the rockyou data breach in 2009. The python scripts allow you to store website credentials such as website name, URL, usernames and passwords. The scripts then check if any of your passwords are shared with those found in the rockyou data breach and alert you.


# Instructions

1. Clone this repository.
2. Extract the Passwords.db from the included database.zip file.
3. Optionally extract rockyou.txt.
4. Run the NewPassword.py script and enter the information.


# Functions of each file

- rockyou.txt - This is a sample of the 32 million breached accounts in the infamous 2009 data breach.
- Passwords.db - This is the database for storing all of the passwords from the rockyou.txt file and the credentials that you wish to check.
- ImportRockyou.py - This is the script I used to import the passwords from the text file into the SQLite3 database.
- CheckPersonal.py - This is the Python script that checks if the credentials you've entered into the script or database are contained in the rockyou table.
- NewPassword.py - This is a script to insert new data into the Personal table to compare to the Rockyou table. This also runs the CheckPersonal.py script.
import sqlite3
import hashlib 

def password_strenght(password):
    if len(password) <=8:
        return("WEAK 🔴")
    has_upper = any(x.isupper() for x in password)
     # any only returns if it is  True and here we are trying to check is there is any capitalized charecters in our password
    has_lower = any(x.islower() for x in password)
    # here we are trying to check is there is any numerical charecters in opur password
    has_digit = any(x.isdigit() or not x.isalnum() for x in password)
    if has_upper and has_lower and has_digit:
        return("STRONG 🟢")
    else:
        return("MEDIUM 🟡")


def main():
    connection = sqlite3.connect("passwords.db")
    # connects the database to the file or creates a new file if dont exit 

    cursor = connection.cursor() 
# this is what helps to execute the sql code below and allows us to write the values in the table 

    #runs the command 
    #autoincrement automatically adds a new number to the ID column for each new entry
    cursor.execute("""
               CREATE TABLE IF NOT EXISTS passwords(
               ID INTEGER PRIMARY KEY AUTOINCREMENT, 
               USERNAME VARCHAR(20) UNIQUE,
               PASSWORDS VARCHAR(255),
               SECURITY_LEVEL VARCHAR(10));
               """)
    connection.commit() # this saves the changes made to the database 
    given = input("Enter Your Paswsword: ")
    username = input("Enter Your Username:")

    hashed_bytes = hashlib.sha256(given.encode())
#given.encode() converts the password text into raw computer data and sha256() scrambles the data completely 

    final_hash = hashed_bytes.hexdigest() 
#turns the scramble into a clean data of 64 charecter 


    outcome = password_strenght(given)
    print(f"Password Strength: {outcome}")

    try: 
        cursor.execute(""
        "INSERT INTO passwords (USERNAME, PASSWORDS, SECURITY_LEVEL) VALUES (?, ?, ?)", (username, final_hash, outcome))
        connection.commit()
        print("Password saved successfully!")
    except sqlite3.IntegrityError:
        print("Error: Username already exists. Please choose a different username.")
        connection.close() # this closes the connection to the database       




# This tells Python to actually start running the main function
if __name__ == "__main__":
    main()
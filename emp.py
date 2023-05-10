import sqlite3
# try:
connection = sqlite3.connect("empDatabase.db")
cursor = connection.cursor()
runStatus = True
while runStatus:
    print(" \n","Menu: \n Type 1 for your entry \n Type 2 for search \n Type 3 for deleting record \n Type 4 for updating a record \n Type 5 for exiting program")
    try:
        menu = float(input("Type Here: "))
        if(menu>5 or menu<1):
            print("Select a value in between 1 to 5")
        else:
            if(menu == 1): #new record
                nameI = input("Enter Your Name: ")
                ageI = input("Enter Your age: ")
                deptI = input("Enter Your Department: ")            
                print(nameI, ageI, deptI)
                try:
                    query = "INSERT into Employee(name, age, dept) values (?, ?, ?)"
                    cursor.execute(query, (nameI, int(ageI), deptI))    
                    connection.commit()
                    print("SUCCESSFULLY SENT")
                except:
                    print("Failed to send data")
            elif(menu == 2): #search
                try:
                    search = float(input("Enter ID: "))
                    query = "SELECT * FROM Employee WHERE id=?"
                    cursor.execute(query, (int(search),))
                    row = cursor.fetchone()
                    if row is None:
                        print("No matching row found.")
                    else:
                        print(f"Name: {row[1]}")
                        print(f"Age: {row[2]}")
                        print(f"Department: {row[3]}")
                except:
                    print("Entered ID isn't valid")
            elif(menu == 3):  #delete
                try:
                    delete = float(input("Enter ID to Delete: "))
                    query = "SELECT * FROM Employee WHERE id=?"
                    cursor.execute(query, (int(delete),))
                    rows = cursor.fetchall()
                    if len(rows) == 0:
                        print("No matching rows found.")
                    else:
                        query = "DELETE FROM Employee WHERE id=?"
                        cursor.execute(query, (int(delete),))
                        connection.commit()
                        print(f"Deleted the row with id {delete}.")
                except:
                    print("Entered ID isn't valid")
            elif(menu == 4): #update
                try:
                    update = input("Enter ID to update an existing record: ")
                    query = "SELECT * FROM Employee WHERE id=?"
                    cursor.execute(query, (int(update),))
                    rows = cursor.fetchall()
                    if len(rows) == 0:
                        print("No matching rows found.")
                    else:
                        name = input("Enter the new name: ")
                        age = input("Enter the new age: ")
                        dept = input("Enter the new department: ")
                        query = "UPDATE Employee SET name=?, age=?, dept=? WHERE id=?"
                        cursor.execute(query, (name, age, dept, int(update)))
                        connection.commit()
                        print(f"Updated the row with id {update}.")
                except:
                    print("Entered ID isn't valid")
            else:
                runStatus = False        
    except:
            print("wrong value entered")




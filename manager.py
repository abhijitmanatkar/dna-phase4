import globals
from validators import *

def getAllMAnagers():
    pass

def getAllManagersByStat():
    # get all managers filtered by a stat
    pass

def insertManager():
    try:
        row = {}
        print("Enter Managers's details: ")
        row["name"] = input("Enter name:")
        row["date_of_birth"] = input("Enter Date of Birth (YYYY-MM-DD):")
        if(ValidateDate(row["date_of_birth"]) == False):
            print("Not a valid Date")
            return False
        row["nationality"] = input("Enter nationality:")
        if(ValidateNationality(row["nationality"])== False):
            print("Not a valid Nationality")
            return False
        row["current_club"] = input("Enter the current_club(press N if no current club) :")
        test = "N"

        if(test == row["current_club"]):
            print("here")
            row["current_club"] = None
            query = "INSERT INTO MANAGER (name, date_of_birth, nationality, current_club) VALUES ('%s', '%s', '%s', %s)" %  (row["name"], row["date_of_birth"], row["nationality"], None)
            print(query)
            globals.cur.execute(query)
            globals.con.commit()
        else:
            query = "INSERT INTO MANAGER (name, date_of_birth, nationality, current_club) VALUES ('%s', '%s', '%s', '%s')" %  (row["name"], row["date_of_birth"], row["nationality"], row["current_club"])
            print(query)
            globals.cur.execute(query)
            globals.con.commit()

        print("Inserted Manager into database")
        return True

    except Exception as e:
        globals.con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return False

def updateManagerClub():
    pass

def deleteManager():
    pass

def updateManagerNationality():
    pass


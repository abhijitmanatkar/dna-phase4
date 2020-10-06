import globals
from validators import *

def getAllOwners():
    pass

def insertOwner():
    try :
        print("Enter Owner details")
        x = input("Enter the Owner Name :")
        y = input("Enter the home country of the owning entity :")
        if(ValidateNationality(y) == False):
            print("Given County is wrong")
            return False

        query = "INSERT INTO OWNER (owner_name,country_origin) VALUES ('%s','%s')" %  (x,y)
        print(query)
        globals.cur.execute(query)
        globals.con.commit()
        print("Inserted owner into database")
        return True



       
    except Exception as e:
        globals.con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return False


def updateOwnerNationality():
    pass

def deleteOwner():
    pass


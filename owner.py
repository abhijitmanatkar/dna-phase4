import globals
from validators import *
from columnar import columnar

def getAllOwners():
    try:
        query = "SELECT * FROM OWNER"
        print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ['Owner ID', 'Name', 'Nationality']
        data = []
        for res in result:
            data.append(list(res.values()))
        table = columnar(data, headers)
        print(table)
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False

def insertOwner():
    pass

def updateOwnerNationality():
    try:
        owner_id = int(input("Enter Owner ID:"))
        q = "SELECT * FROM OWNER WHERE owner_id=%d" % (owner_id)
        globals.cur.execute(q)
        owner = globals.cur.fetchone()
        if owner is None:
            print("Not found")
            return False
        newNationality = input("Enter new nationality:")
        if not ValidateNationality(newNationality):
            print("Not a valid nationality")
            return False
        query = "UPDATE OWNER SET nationality='%s' WHERE owner_id=%d" % (newNationality, owner_id)
        globals.cur.execute(query)
        globals.con.commit()

        print("Nationality updated")
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to update")
        print(">>>>>>>>>>>>>", e)
        return False

def deleteOwner():
    pass


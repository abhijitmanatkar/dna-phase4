import globals
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
    pass

def deleteOwner():
    pass


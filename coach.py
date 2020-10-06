import globals
from validators import *
from columnar import columnar

def getAllCoaches():
    try:
        query = "SELECT * FROM COACH"
        print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ['Name', 'Manager Name', 'Nationality', 'Designation', 'DOB']
        data = []
        for res in result:
            try:
                q = "SELECT name FROM MANAGER WHERE manager_id=%d" % (res["manager_id"])
                globals.cur.execute(q)
                res["manager_id"] = globals.cur.fetchone()["name"]
            except:
                res["manager_id"] = "" 
            reslist = list(res.values())
            data.append(reslist)
        table = columnar(data, headers)
        print(table)
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False

def insertCoach():
    pass

def updateCoachNationality():
    try:
        name = input("Enter Coach Name:")
        manager_id = int(input("Enter manager ID:"))
        q = "SELECT * FROM COACH WHERE manager_id=%d AND name='%s'" % (manager_id, name)
        globals.cur.execute(q)
        coach = globals.cur.fetchone()
        if coach is None:
            print("Not found")
            return False
        newNationality = input("Enter new nationality:")
        if not ValidateNationality(newNationality):
            print("Not a valid nationality")
            return False
        query = "UPDATE COACH SET nationality='%s' WHERE name='%s' AND manager_id=%d" % (newNationality, name, manager_id)
        globals.cur.execute(query)
        globals.con.commit()

        print("Nationality updated")
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to update")
        print(">>>>>>>>>>>>>", e)
        return False

def deleteCoach():
    pass


import globals
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
    pass

def deleteCoach():
    pass


import globals
from columnar import columnar

def getAllClubs():
    try:
        query = "SELECT * FROM CLUB"
        print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ['Club ID', 'Name', 'Home Ground', 'Foundation Year', 'Street Address', 'Zip Code', 'City', 'Country']
        data = []
        for res in result:
            try:
                q = "SELECT * FROM ZIP_MAP WHERE zip_code='%s'" % (res["zip_code"])
                globals.cur.execute(q)
                zip_map = globals.cur.fetchone()
                res["city"] = zip_map["city"]
                res["country"] = zip_map["country"]
            except:
                res["city"] = ""
                res["country"] = ""
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

def insertClub():
    pass

def searchClub():
    pass

def deleteClub():
    pass

def getClubPlayersBySeason():
    pass

def getPlayersSoldByClub():
    pass

def getPlayersBoughtByClub():
    pass

def getAllClubTransfers():
    pass

def getClubNetSpent():
    pass

def getClubPerformanceInTournament():
    pass
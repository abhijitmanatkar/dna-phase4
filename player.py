import globals
from validators import *
from columnar import columnar

def getPositions(player_id):
    try:
        positions = ""
        q = "SELECT position_name FROM POSITIONS WHERE player_id=%d" % (player_id)
        globals.cur.execute(q)
        result = globals.cur.fetchall()
        for pos in result:
            positions += pos["position_name"] + " "
        return positions
    except:
        return ""

def getAllPlayers():
    try:
        query = "SELECT * FROM PLAYER"
        print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ['Player ID', 'Name', 'DOB', 'Nationality', 'Agent Name', 'Positions']
        data = []
        for res in result:
            agent_id = res["agent_id"]
            try:
                q = "SELECT name FROM AGENT WHERE agent_id=%d" % (agent_id)
                globals.cur.execute(q)
                res["agent_id"] = globals.cur.fetchone()["name"]
            except:
                res["agent_id"] = ""
            res["positions"] = getPositions(res["player_id"])
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

def getAllPlayersByStat():
    # return all players filtered by a stat
    pass

def getAllPlayersByCountry():
    pass

def updatePlayerNationality():
    try:
        player_id = int(input("Enter player ID:"))
        q = "SELECT * FROM PLAYER WHERE player_id=%d" % (player_id)
        globals.cur.execute(q)
        player = globals.cur.fetchone()
        if player is None:
            print("Not found")
            return False
        newNationality = input("Enter new nationality:")
        if not ValidateNationality(newNationality):
            print("Not a valid nationality")
            return False
        query = "UPDATE PLAYER SET nationality='%s' WHERE player_id=%d" % (newNationality, player_id)
        globals.cur.execute(query)
        globals.con.commit()

        print("Nationality updated")
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to update")
        print(">>>>>>>>>>>>>", e)
        return False

def searchPlayer():
    pass

def insertPlayer():
    pass

def getPlayerStatsBySeason():
    pass

def getPlayerStatsPer90():
    pass

def getPlayerCareerStats():
    pass

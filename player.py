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
    try:
        print("Select which statistic to use:")
        print("1. Goals")
        print("2. Assists")
        print("3. Saves")
        print("4. Tackles")
        print("5. Clearances")
        print("6. Red Cards")
        print("7. Yellow Cards")
        print("8. Minutes played")

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
    try:
        row = {}
        print("Enter Player's details: ")
        row["player_name"] = input("Enter name:")
        row["date_of_birth"] = input("Enter Date of Birth (YYYY-MM-DD):")
        if(ValidateDate(row["date_of_birth"]) == False):
            print("Not a valid Date")
            return False
        row["nationality"] = input("Enter nationality:")
        if(ValidateNationality(row["nationality"])== False):
            print("Not a valid Nationality")
            return False
        row["agent_id"] = input("Enter the agent_id :")
        globals.cur.execute('SELECT * FROM AGENT')
        temp = globals.cur.fetchall()
        flag = False
        for i in temp:
            if(int(i["agent_id"]) == int(row["agent_id"])):
                flag = True
                break
        if(flag == True):
            query = "INSERT INTO PLAYER (player_name, date_of_birth, nationality, agent_id) VALUES ('%s', '%s', '%s', %s)" %  (row["player_name"], row["date_of_birth"], row["nationality"], row["agent_id"])
            print(query)
            globals.cur.execute(query)
            globals.con.commit()
            print("Inserted Player into database")
            return True
        else:
            
            print("Agent Id given is wrong")
            return False

    except Exception as e:
        globals.con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return False

def getPlayerStatsBySeason():
    try:
        player_id = int(input("Enter player id:"))
        season_year = input("Enter season year:")
        query = "SELECT PLAYER.player_name,minutes_played,goals,assists,clearances,tackles,red_cards,yellow_cards,saves FROM PLAYER INNER JOIN PLAYED_FOR ON PLAYER.player_id=%d AND season_year='%s'" % (player_id, season_year)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ["Name", "Minutes played", "Goals", "Assists", "Clearances", "Tackles", "Red cards", "Yellow cards", "Saves"]
        data = []
        for res in result:
            data.append(list(res.values()))
        if len(data) > 0:
            for i in range(1,len(data)):
                for j in range(1,9):
                    data[0][j] += data[i][j]
            data = data[0:1]
        table = columnar(data, headers)
        print(table)
    
    except Exception as e:
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
        return False


def getPlayerStatsPer90():
    pass

def getPlayerCareerStats():
    pass

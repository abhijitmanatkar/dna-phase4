import globals
from validators import *
def getAllPlayers():
    pass

def getAllPlayersByStat():
    # return all players filtered by a stat
    pass

def getAllPlayersByCountry():
    pass

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
    pass

def getPlayerStatsPer90():
    pass

def getPlayerCareerStats():
    pass

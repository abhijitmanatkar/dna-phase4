import globals
from validators import *
from columnar import columnar

def insertSeason():
    try :
        x = input("Enter the season :")
        y = x.replace(" ","")
        x = y
        if(ValidateSeasonYear(x) == False):
            print("Wrong Format for season")
            return False
        query = "INSERT INTO SEASON (season_year) VALUES ('%s')" %  (x)
        print(query)
        globals.cur.execute(query)
        globals.con.commit()
        print("Inserted season into database")
        return True



       
    except Exception as e:
        globals.con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return False
        
        


def getAllTournaments():
    try:
        query = "SELECT * FROM TOURNAMENT"
        print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ['Tournament Name', 'Number of Participants', 'Tournament Type']
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


def getTournamentTeamsBySeason():
    pass


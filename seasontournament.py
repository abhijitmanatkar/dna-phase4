import globals
from validators import *

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
        
        


def getTournamentTeamsBySeason():
    pass


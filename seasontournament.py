import globals
from columnar import columnar

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

def addSeason():
    pass

def getTournamentTeamsBySeason():
    pass


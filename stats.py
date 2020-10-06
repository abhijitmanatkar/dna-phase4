import globals
from columnar import columnar

def getTransfersByPriceRange():
    try:
        low = int(input("Enter minimum price:"))
        high = int(input("Enter maximum price:"))
        query = "SELECT PLAYER.player_name,CLUB_FROM.club_name,CLUB_TO.club_name,AGENT.name,transfer_fee,agent_fee,date_of_transfer\
                FROM TRANSFER\
                INNER JOIN PLAYER ON TRANSFER.player_id=PLAYER.player_id\
                INNER JOIN CLUB CLUB_FROM ON TRANSFER.club_from_id=CLUB_FROM.club_id\
                INNER JOIN CLUB CLUB_TO ON TRANSFER.club_to_id=CLUB_TO.club_id\
                INNER JOIN AGENT ON TRANSFER.agent_id=AGENT.agent_id\
                WHERE transfer_fee>=%d AND transfer_fee<=%d" % (low, high)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ["Name", "From", "To", "Agent", "Transfer fee", "Agent Fee", "Transfer"]
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


def getMaxGoalsPlayerInSeason():
    pass

def getMaxAssistsPlayerInSeason():
    pass

def getMinYellowCardsPlayerInSeason():
    pass
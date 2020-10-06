import globals
from validators import *
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
    try:
        row = {}
        print("Enter Club details: ")
        row["club_name"] = input("Enter club name:")
        row["foundation_year"] = input("Enter Foundation year of club:")
        row["city"] = input("Enter the City the club belongs to:")
        row["street_address"] = input("Enter the street Address of the club headquarters:")
        row["zip_code"] = input("Enter the zip code of the club headquarters:")
        row["home_ground"] = input("Enter the home ground :")
        row["country"] = input("Enter the home country:")
        if(ValidateNationality(row["country"])== False):
            print("Not a valid Country Name")
            return False
        

        globals.cur.execute('SELECT * FROM ZIP_MAP')
        temp = globals.cur.fetchall()
        flag = False
        #print(row["manager_id"])
        for t in temp:
            #print("manager_id : %d" % t["manager_id"])
            if((t["zip_code"]) == (row["zip_code"])):
                flag = True
               # print("inside")
                break
        if(flag == False):
            query1 = "INSERT INTO ZIP_MAP (zip_code,city,country) VALUES ('%s', '%s', '%s')" % (row["zip_code"],row["city"],row["country"])        
            print(query1)
            globals.cur.execute(query1)
            globals.con.commit()
        query = "INSERT INTO CLUB (club_name,home_ground,foundation_year,zip_code,street_address) VALUES ('%s', '%s', '%s', '%s', '%s')" %  (row["club_name"], row["home_ground"], row["foundation_year"], row["zip_code"],row['street_address'])
        print(query)
        globals.cur.execute(query)
        globals.con.commit()
        print("Inserted CLUB into database")
        return True



       
    except Exception as e:
        globals.con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return False
    

def searchClub():
    pass

def deleteClub():
    try :
        x = int(input("Enter club_id of the Club to be deleted"))
        query1 = "DELETE FROM TRANSFER WHERE club_from_id = %d " % (x)
        query7 = "DELETE FROM TRANSFER WHERE club_to_id = %d " % (x)
        query = "DELETE FROM CLUB WHERE club_id = %d " % (x)
        query2 = "DELETE FROM MANAGES WHERE club_id = %d " % (x)
        query3 = "DELETE FROM OWNS WHERE club_id = %d " % (x)
        query4 = "DELETE FROM PLAYED_IN_KNOCKOUT WHERE club_id = %d " % (x)
        query5 = "DELETE FROM PLAYED_IN_LEAGUE WHERE club_id = %d " % (x)
        query6 = "DELETE FROM PLAYED_FOR WHERE club_id = %d " % (x)
        
        globals.cur.execute(query1)
        globals.cur.execute(query2)
        globals.cur.execute(query3)
        globals.cur.execute(query4)
        globals.cur.execute(query5)
        globals.cur.execute(query6)
        globals.cur.execute(query7)
        globals.cur.execute(query)
        globals.con.commit()
        print("Club Deleted")
    except Exception as e:
        globals.con.rollback()
        print("Failed to Delete")
        print(">>>>>>>>>>>>>", e)
        return False


def getClubPlayersBySeason():
    try:
        club_id = int(input("Enter club id:"))
        season_year = input("Enter a season year (20XX-YY):")
        query = "SELECT PLAYER.player_name,minutes_played,goals,assists,clearances,tackles,red_cards,yellow_cards,saves FROM PLAYER INNER JOIN PLAYED_FOR ON PLAYER.player_id=PLAYED_FOR.player_id AND season_year='%s' AND club_id=%d" % (season_year, club_id)
        print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ["Name", "Minutes played", "Goals", "Assists", "Clearances", "Tackles", "Red cards", "Yellow cards", "Saves"]
        data = []
        for res in result:
            data.append(list(res.values()))
        table = columnar(data, headers)
        print(table)
        return True
    
    except Exception as e:
        print("Failed to retreive from database")
        print(">>>>>>>>>>>>>", e)
        return False

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
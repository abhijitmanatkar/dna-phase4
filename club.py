import globals
from validators import *

def getAllClubs():
    pass

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
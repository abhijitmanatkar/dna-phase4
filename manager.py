import globals
from validators import *
from columnar import columnar

def getAllManagers():
    try:
        query = "SELECT * FROM MANAGER"
        print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ['Manager ID', 'Name', 'Nationality', 'Current Club', 'DOB']
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

def getAllManagersByStat():
    # get all managers filtered by a stat
    pass

def insertManager():
    try:
        row = {}
        print("Enter Managers's details: ")
        row["name"] = input("Enter name:")
        row["date_of_birth"] = input("Enter Date of Birth (YYYY-MM-DD):")
        if(ValidateDate(row["date_of_birth"]) == False):
            print("Not a valid Date")
            return False
        row["nationality"] = input("Enter nationality:")
        if(ValidateNationality(row["nationality"])== False):
            print("Not a valid Nationality")
            return False
        row["current_club"] = input("Enter the current_club(press N if no current club) :")
        test = "N"

        if(test == row["current_club"]):
            print("here")
            row["current_club"] = None
            query = "INSERT INTO MANAGER (name, date_of_birth, nationality, current_club) VALUES ('%s', '%s', '%s', %s)" %  (row["name"], row["date_of_birth"], row["nationality"], None)
            print(query)
            globals.cur.execute(query)
            globals.con.commit()
        else:
            query = "INSERT INTO MANAGER (name, date_of_birth, nationality, current_club) VALUES ('%s', '%s', '%s', '%s')" %  (row["name"], row["date_of_birth"], row["nationality"], row["current_club"])
            print(query)
            globals.cur.execute(query)
            globals.con.commit()

        print("Inserted Manager into database")
        return True

    except Exception as e:
        globals.con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return False

def updateManagerClub():
    try:
        manager_id = int(input("Enter Manager ID:"))
        q = "SELECT * FROM MANAGER WHERE manager_id=%d" % (manager_id)
        globals.cur.execute(q)
        manager = globals.cur.fetchone()
        if manager is None:
            print("Not found")
            return False
        
        club_id = int(input("Enter new club ID:"))
        q = "SELECT * FROM CLUB WHERE club_id=%d" % club_id
        globals.cur.execute(q)
        club = globals.cur.fetchone()
        if club is None:
            print("Not a valid club")
            return False
         
        season_year = input("Enter current season year (20XX-YY):")
        if not ValidateSeasonYear(season_year):
            print("Not a valid season year")
            return False
        q = "SELECT * FROM SEASON WHERE season_year='%s'" % (season_year)
        globals.cur.execute(q)
        season = globals.cur.fetchone()
        if season is None:
            q = "INSERT INTO SEASON (season_year) VALUES ('%s')" % (season_year)
            globals.cur.execute(q)
    
        query = "UPDATE MANAGER SET current_club='%s' WHERE manager_id=%d" % (club["club_name"], manager_id)
        globals.cur.execute(query)

        query = "INSERT INTO MANAGES (manager_id, club_id, season_year) VALUES ('%d', '%d', '%s')" % (manager_id, club_id, season_year)
        globals.cur.execute(query)

        globals.con.commit()

        print("Current club updated")
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to update")
        print(">>>>>>>>>>>>>", e)
        return False

def deleteManager():
    pass

def updateManagerNationality():
    try:
        manager_id = int(input("Enter Manager ID:"))
        q = "SELECT * FROM MANAGER WHERE manager_id=%d" % (manager_id)
        globals.cur.execute(q)
        manager = globals.cur.fetchone()
        if manager is None:
            print("Not found")
            return False
        newNationality = input("Enter new nationality:")
        if not ValidateNationality(newNationality):
            print("Not a valid nationality")
            return False
        query = "UPDATE MANAGER SET nationality='%s' WHERE manager_id=%d" % (newNationality, manager_id)
        globals.cur.execute(query)
        globals.con.commit()

        print("Nationality updated")
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to update")
        print(">>>>>>>>>>>>>", e)
        return False


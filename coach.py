import globals
from validators import *
def getAllCoaches():
    pass

def insertCoach():
    try:
        row = {}
        print("Enter Coach details: ")
        row["name"] = input("Enter name:")
        row["date_of_birth"] = input("Enter Date of Birth (YYYY-MM-DD):")
        if(ValidateDate(row["date_of_birth"]) == False):
            print("Not a valid Date")
            return False
        row["nationality"] = input("Enter nationality:")
        if(ValidateNationality(row["nationality"])== False):
            print("Not a valid Nationality")
            return False
        row["designation"] = input("Enter the designation :")
        row["manager_id"] = input("Enter the Manager_id of the Manager under whom the coach works:")

        globals.cur.execute('SELECT * FROM MANAGER')
        temp = globals.cur.fetchall()
        flag = False
        #print(row["manager_id"])
        for t in temp:
            #print("manager_id : %d" % t["manager_id"])
            if(int(t["manager_id"]) == int(row["manager_id"])):
                flag = True
               # print("inside")
                break
        if(flag == True):        
    
            query = "INSERT INTO COACH (name, date_of_birth, nationality, designation, manager_id) VALUES ('%s', '%s', '%s', '%s', '%s')" %  (row["name"], row["date_of_birth"], row["nationality"], row["designation"],row['manager_id'])
            print(query)
            globals.cur.execute(query)
            globals.con.commit()
            print("Inserted coach into database")
            return True

        else:
            print("Manager_id given is wrong")
            return False

       
    except Exception as e:
        globals.con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return False

def updateCoachNationality():
    pass

def deleteCoach():
    pass


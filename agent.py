import globals

def getAllAgents():
    pass

def insertAgent():
    try:
        row = {}
        print("Enter agent's details: ")
        row["name"] = input("Enter name:")
        row["data_of_birth"] = input("Enter Date of Birth (YYYY-MM-DD):") 
        row["nationality"] = input("Enter nationality:")

        query = "INSERT INTO AGENT (name, data_of_birth, nationality) VALUES ('%s', '%s', '%s')" %  (row["name"], row["data_of_birth"], row["nationality"])
        print(query)
        globals.cur.execute(query)
        globals.con.commit()

        print("Inserted agent into database")
        return True

    except Exception as e:
        globals.con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return False

def deleteAgent():
    pass

def updateAgentNationality():
    pass


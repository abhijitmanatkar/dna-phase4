import globals
from validators import *
from columnar import columnar

def getAllAgents():
    try:
        query = "SELECT * FROM AGENT"
        print(query)
        globals.cur.execute(query)
        result = globals.cur.fetchall()
        headers = ['Agent ID', 'Name', 'DOB', 'Nationality']
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
        

def insertAgent():
    try:
        row = {}
        print("Enter agent's details: ")
        row["name"] = input("Enter name:")
        row["data_of_birth"] = input("Enter Date of Birth (YYYY-MM-DD):")
        if not ValidateDate(row["data_of_birth"]):
            print("Not a valid date")
            return False
        row["nationality"] = input("Enter nationality:")
        if not ValidateNationality(row["nationality"]):
            print("Not a valid nationality")
            return False

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
        try :
            x = int(input("Enter agent_id of the agent to be deleted: "))
            query1 = "DELETE FROM AGENT WHERE agent_id = %d " % (x)
            query2 = "DELETE FROM TRANSFER WHERE agent_id = %d " % (x)
            query = "UPDATE PLAYER SET agent_id = NULL WHERE agent_id =  %d" % (x)
        
            globals.cur.execute(query)
            globals.cur.execute(query2)
            globals.cur.execute(query1)
            
            globals.con.commit()
            print("Agent with given Id doesnot exist anymore")
            return True
        except Exception as e:
            globals.con.rollback()
            print("Failed to Delete")
            print(">>>>>>>>>>>>>", e)
            return False

def updateAgentNationality():
    try:
        agent_id = int(input("Enter Agent ID:"))
        q = "SELECT * FROM AGENT WHERE agent_id=%d" % (agent_id)
        globals.cur.execute(q)
        agent = globals.cur.fetchone()
        if agent is None:
            print("Not found")
            return False
        newNationality = input("Enter new nationality:")
        if not ValidateNationality(newNationality):
            print("Not a valid nationality")
            return False
        query = "UPDATE AGENT SET nationality='%s' WHERE agent_id=%d" % (newNationality, agent_id)
        globals.cur.execute(query)
        globals.con.commit()

        print("Nationality updated")
        return True
    
    except Exception as e:
        globals.con.rollback()
        print("Failed to update")
        print(">>>>>>>>>>>>>", e)
        return False



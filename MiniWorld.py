import subprocess as sp
import pymysql
import pymysql.cursors
import globals
from agent import *


def option2():
    """
    Function to implement option 1
    """
    print("Not implemented")


def option3():
    """
    Function to implement option 2
    """
    print("Not implemented")


def option4():
    """
    Function to implement option 3
    """
    print("Not implemented")

        

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        insertAgent()
    elif(ch == 2):
        option2()
    elif(ch == 3):
        option3()
    elif(ch == 4):
        option4()
    elif(ch == 5):
        option4()
    elif(ch == 6):
        option4()
    elif(ch == 7):
        option4()
    elif(ch == 8):
        option4()
    elif(ch == 9):
        option4()
    elif(ch == 10):
        option4()
    elif(ch == 11):
        option4()
    elif(ch == 12):
        option4()
    elif(ch == 13):
        option4()
    elif(ch == 14):
        option4()
    elif(ch == 15):
        option4()
    elif(ch == 16):
        option2()
    elif(ch == 17):
        option3()
    elif(ch == 18):
        option4()
    elif(ch == 19):
        option4()
    elif(ch == 20):
        option4()
    elif(ch == 21):
        option4()
    elif(ch == 22):
        option4()
    elif(ch == 23):
        option4()
    elif(ch == 24):
        option4()
    elif(ch == 25):
        option4()
    elif(ch == 26):
        option4()
    elif(ch == 27):
        option4()
    elif(ch == 28):
        option4()
    elif(ch == 29):
        option4()
    elif(ch == 30):
        option4()
    elif(ch == 31):
        option4()
    elif(ch == 32):
        option4()
    elif(ch == 33):
        option4()
    elif(ch == 34):
        option4()
    elif(ch == 35):
        option4()
    elif(ch == 36):
        option4()
    elif(ch == 37):
        option5()
    elif(ch == 31):
        option4()
    elif(ch == 32):
        option4()
    elif(ch == 33):
        option4()
    elif(ch == 34):
        option4()
    elif(ch == 35):
        option4()
    elif(ch == 36):
        option4()
    elif(ch == 37):
        option5()
    elif(ch == 38):
        option4()
    elif(ch == 39):
        option4()
    elif(ch == 40):
        option4()
    elif(ch == 41):
        option4()
    elif(ch == 42):
        option4()
    elif(ch == 43):
        option4()
    elif(ch == 44):
        option4()
    elif(ch == 45):
        option4()
        
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        globals.con = pymysql.connect(host='sql12.freesqldatabase.com',
                              user='sql12368590',
                              password='EuQ3fsLRGW',
                              db='sql12368590',
                              port=3306,
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(globals.con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with globals.con.cursor() as globals.cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # The options presented for database operation
                print("1. Add Agent")  # insert agent 
                print("2. Add Player")  
                print("3. Add Club")  # Promote Employee
                print("4. Add Owner")  # Employee Statistics
                print("5. Add Coach")
                print("6. Add Season")
                print("7. Add Manager")
                print("8. Update Nationality of Manager")
                print("9. Update Nationality of Player")
                print("10. Update Nationality of Owner")
                print("11. Update Nationality of Coach")
                print("12. Update Nationality of Agent")
                print("13. Update Current Club of a Manager")
                print("14. Delete Club")
                print("15. Delete Player")
                print("16. Delete Manager")
                print("17. Delete Owner")
                print("18. Delete Agent")
                print("19. Delete Coach")
                print("20. Display teams in a tournament")
                print("21. Display Squad of a club")
                print("22. Display Player performance for a season")
                print("23. Display Transfer out of a club")
                print("24. Display all Transfer of a club")
                print("25. Display Transfer in of a club")
                print("26. Display all players of a country")
                print("27. Filter players by a given statistic")
                print("28. Filter Transfers by Price Range")
                print("29. Filter Managers by statistic")
                print("30. Display Goals/90 and Assist/90")
                print("31. Show player with  most goals")
                print("32. Show player with Highest Assists")
                print("33. Show player with least yellow cards")
                print("34. Display Career stats for a given Player")
                print("35. Return Net Spent of a Club")
                print("36. Search Player")
                print("37. Search Club")
                print("38. Show all Players")
                print("39. Show all Coaches")
                print("40. Show all Manager")
                print("41. Show all Owner")
                print("42. Show all Agents")
                print("43. Show all Clubs")
                print("44. Show all Tournament")
                print("45. Show Club results in a tournament")

                print("46. Logout")
                
                


                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 46:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")
            globals.con.close()

    except:
        #tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")

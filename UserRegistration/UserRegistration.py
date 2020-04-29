# =======================================================================
# title           : UserRegistration.py
# description     : This program displays an interactive menu on
# usage           : python UserRegistration
# author          : HappyByte
# =======================================================================

# Import the modules needed to run the script.
import os
import time

# Custom Imports
from pprint import pprint
from DataStructures import UserIdGenerator, UserDictionary, SingleUser

# GLOBAL CLASSES
userdictionary = UserDictionary()
useridgenerator = UserIdGenerator()


# Yield
def yieldQuery():
    time.sleep(2)  # Delay for 1 seconds.


# Execute menu
def exec_choice(choice):
    os.system('clear')

    ch = choice

    if ch == '':
        pprint("WARNING: NEED AT LEAST ONE CHOICE")
        yieldQuery()
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            pprint("Invalid selection, please try again.")
            yieldQuery()
            menu_actions['main_menu']()
    return


def createMenu():
    os.system('clear')

    pprint("----------- USER REGISTRATION -----")
    pprint("1. {0:>4}".format("readUserById"))
    pprint("2. {0:>4}".format("updateOrAddUser"))
    pprint("3. {0:>4}".format("deleteUser"))
    pprint("4. {0:>4}".format("readAllUsers"))
    pprint("5. {0:>4}".format("deleteAllUsers"))
    pprint("6. {0:>4}".format("countUsers"))
    pprint("Q. {0:>4}".format("Quit"))
    pprint("-----------------------------------")

    choice = input("Chose Option: ")
    exec_choice(choice)
    createMenu()
    return


def readUser():
    userid = int(input("userid: "))
    userdictionary.readUser(userid)
    input("Press Enter to Continue")
    return


def deleteUser():
    userid = int(input("userid: "))
    userdictionary.deleteUser(userid)
    pprint("Deleted User by ID")
    yieldQuery()
    return


def updateOrAddUser():
    username = input("username: ")
    age = int(input("age: "))
    location = input("location: ")

    # save user in memory & return
    incrementalId = useridgenerator.getNewId()
    userdictionary.updateOrAddUser(username, age, location, incrementalId)
    pprint("User by ID {0} Added to database".format(incrementalId))
    yieldQuery()
    return


def readMultipleUsers():
    userdictionary.readAllUsers()
    input("Press ENTER to Continue")
    return


def deleteAllUsers():
    userdictionary.deleteAllUsers()
    pprint(" All Users Deleted ")
    yieldQuery()
    return


def countUsers():
    userdictionary.countUsers()
    yieldQuery()
    return


def exit():
    pprint("GOOD BYE ! ! !")
    quit()


menu_actions = {
    'main_menu': createMenu,
    '1': readUser,
    '2': updateOrAddUser,
    '3': deleteUser,
    '4': readMultipleUsers,
    '5': deleteAllUsers,
    '6': countUsers,
    'Q': exit,
}

# =======================================================================
# Main Program
# =======================================================================
if __name__ == "__main__":
    # Launch main menu
    createMenu()

# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Load account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. Block a friend")
    print("5. View blocked friends")
    print("6. Unblock a friend")
    print("7. Send a message to a friend")
    print("8. Save account")
    print("9. Delete account")
    print("10. <- Go back ")
    return input("Please Choose a number: ")

#Various import Statements can go here
from social_network_classes import SocialMedia
import social_network_ui
import time

def manageAccount():
    manege_menu_choice = social_network_ui.manageAccountMenu()
    while True:
        if manege_menu_choice == "1":
            print("EDITING ACCOUNT DETAILS... \n")
            x_name = input("Please enter your new name: \n")
            x_age = 0
            while True:
                x = input("Please enter your new age: \n")
                if x.isnumeric():
                    x_age = x
                    break
            x_acc_name = input("Please enter your new accout name: \n")
            socialNetwork.createAccount(x_name, x_age, x_acc_name)
            manege_menu_choice = social_network_ui.manageAccountMenu()

        elif manege_menu_choice == "2":
            print("ADDING A NEW FRIEND...\n")
            x_friend_name = input('Enter the account name of your friend \n')
            socialNetwork.addNewFriend(x_friend_name)
            print("New friend " + x_friend_name + " added to your friends list")
            manege_menu_choice = social_network_ui.manageAccountMenu()

        elif manege_menu_choice == "3":
            print("PRINTING FRIENDS LIST... \n")
            socialNetwork.printFriends(True)
            manege_menu_choice = social_network_ui.manageAccountMenu()
        
        elif manege_menu_choice == "4":
            print("BLOCK FRIEND MENU... \n")
            while True:
                x_blocked_name = input("What is the account name of your friend? \n")
                var = socialNetwork.blockFriend(x_blocked_name, True)
                if var:
                    break
            manege_menu_choice = social_network_ui.manageAccountMenu()

        elif manege_menu_choice == "5":
            print("PRINTING BLOCKED FRIENDS LIST... \n")
            socialNetwork.printFriends(False)
            manege_menu_choice = social_network_ui.manageAccountMenu()
        
        elif manege_menu_choice == "6":
            print("UNBLOCK A FRIEND MENU... \n")
            while True:
                    x_blocked_name = input("What is the account name of your friend? \n")
                    var = socialNetwork.blockFriend(x_blocked_name, False)
                    if var:
                        break
            manege_menu_choice = social_network_ui.manageAccountMenu()
        
        elif manege_menu_choice == "7":
            print("SEND A MESSAGE TO A FRIEND ... \n")
            while True:
                x_fr_name = input('Which friend do you want to message?: \n')
                x_text = input("Enter message: \n")
                var = socialNetwork.sendMessage(x_fr_name, x_text)
                if var:
                    break
                else:
                    print("ERROR: No friend with the name " + x_fr_name)
            manege_menu_choice = social_network_ui.manageAccountMenu()
        
        elif manege_menu_choice == "8":
            print("Saving Account...\n")
            time.sleep(2)
            socialNetwork.saveAccount()
            break



            

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    socialNetwork = SocialMedia()
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    if(socialNetwork.getAccountDetails()[0] == None and socialNetwork.getAccountDetails()[1] == None and socialNetwork.getAccountDetails()[2] == None):
        choice = social_network_ui.mainMenu()
    else:
        socialNetwork.deleteAccount()
        choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu... \n")
            x_name = input("Please enter your name: \n")
            x_age = 0
            while True:
                x = input("Please enter your age: \n")
                if x.isnumeric():
                    x_age = x
                    break
            x_acc_name = input("Please enter your accout name: \n")
            socialNetwork.createAccount(x_name, x_age, x_acc_name)
            manageAccount()


        elif choice == "2":
            print("\n You are now in the load account menu... \n")
            while True:
                x_acc_name = input("Please enter the account name you want to load: \n")
                var = socialNetwork.loadAccount(x_acc_name)
                if var:
                    print("Successfully loaded account " + x_acc_name)
                    manageAccount()
                    break
                else:
                    print("Account " + x_acc_name + " doesn't exist")

        elif choice == "3":
            print("Thank you for visiting. Goodbye3")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()




        

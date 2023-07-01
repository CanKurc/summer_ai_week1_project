import json
import os

class SocialMedia:
    def __init__(self):
        self.name = None
        self.age = None
        self.account_name = None
        self.friends = []
        self.blockedFriends = []
    
    def createAccount(self, name, age, account_name):
        self.name = name
        self.age = age
        self.account_name = account_name
        print("account name is: " + self.name)

    def getAccountDetails(self):
        return [self.name, self.age, self.account_name, self.friends, self.blockedFriends]
    
    def addNewFriend(self, friend_acc_name):
        self.friends.append(friend_acc_name)

    def printFriends(self, realFriends):
        if realFriends:
            if (len(self.friends) == 0):
                print('YOU HAVE NO FRIENDS')
            else:
                for i in self.friends:
                    print(i)
        else:
            if (len(self.blockedFriends) == 0):
                print('YOU HAVE NO BLOCKED FRIENDS')
            else:
                for i in self.blockedFriends:
                    print(i)

    def blockFriend(self, blocked_friend_acc_name, blockFriend):
        if blockFriend:
            x = False
            for i in self.friends:
                if (i == blocked_friend_acc_name):
                    self.blockedFriends.append(blocked_friend_acc_name)
                    self.friends.remove(i)
                    x = True
                    break
            if(x):
                print("Successfully blocked friend " + blocked_friend_acc_name)
                return True
            else:
                print(blocked_friend_acc_name + " was not a friend, couldn't block")
                return False
        else:
            x = False
            for i in self.blockedFriends:
                if (i == blocked_friend_acc_name):
                    self.friends.append(blocked_friend_acc_name)
                    self.blockedFriends.remove(i)
                    x = True
                    break
            if(x):
                print("Successfully unblocked friend " + blocked_friend_acc_name)
                return True
            else:
                print(blocked_friend_acc_name + " was not a friend, couldn't unblock")
                return False       

    def sendMessage(self, friend_acc_name, message):
        x = False
        for i in self.friends:
            if (i == friend_acc_name):
                print("MESSAGE SENT: \n " + message + "\n To friend " + i)
                x = True

        return x


    def saveAccount(self):
        array = []
        small_array = []
        if os.path.exists("sample.json"):
            # Opening JSON file
            with open('sample.json', 'r') as file:
                v = json.loads("\n".join(file.readlines()))
                array = (v["array"])

        small_array.append(self.name)
        small_array.append(self.age)
        small_array.append(self.account_name)
        small_array.append(self.friends)
        small_array.append(self.blockedFriends)

        array.append(small_array)

        dict = {
            "array": array
        }
        # Serializing json
        json_object = json.dumps(dict, indent=1)
        
        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
        
        print("Account save successful...")
            
    def loadAccount(self, account_name):
        x = False
        array = []
        if os.path.exists("sample.json"):
            # Opening JSON file
            with open('sample.json', 'r') as file:
                v = json.loads("\n".join(file.readlines()))
                array = (v["array"])
        
        for i in array:
            if(i[2] == account_name):
                x = True
                self.name = i[0]
                self.age = i[1]
                self.account_name = i[2]
                self.friends = i[3]
                self.blockedFriends = i[4]
                array.remove(i)
                dict = {
                    "array": array
                }
                # Serializing json
                json_object = json.dumps(dict, indent=1)
                
                # Writing to sample.json
                with open("sample.json", "w") as outfile:
                    outfile.write(json_object)
                        
        return x



    def deleteAccount(self):
        self.name = None
        self.age = None
        self.account_name = None
        self.friends = None
        self.blockedFriends = None
        dictionary = {}
        json_object = json.dumps(dictionary, indent=5)
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
        print("Account successfully deleted...")
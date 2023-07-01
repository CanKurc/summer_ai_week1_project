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
        # Data to be written
        dictionary = {
            "name": self.name,
            "age": self.age,
            "account_name": self.account_name,
            "friends": self.friends,
            "blocked_friends": self.blockedFriends
        }
        
        # Serializing json
        json_object = json.dumps(dictionary, indent=5)
        
        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
        
        print("Account save successful...")
            
    def loadAccount(self, account_name):
        x = False
        if os.path.exists("sample.json"):
            # Opening JSON file
            with open('sample.json', 'r') as file:
                v = json.loads("\n".join(file.readlines()))
                if account_name == v["account_name"]:
                    x = True
                    if x:
                        self.name = v["name"]
                        self.age = v["age"]
                        self.account_name = v["account_name"]
                        self.friends = v["friends"]
                        self.blockedFriends = v["blocked_friends"]
                        
        return x



    def deleteAccount(self):
        self.name = None
        self.age = None
        self.account_name = None
        self.friends = None
        self.blockedFriends = None
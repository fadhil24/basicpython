class Application():
    def __init__(self):
        self.username = "alpro"
        self.password = "daspro"

    def Login(self,username,password):
        if (self.username == username) and (self.password == pw):
            print("Login Success\nWelcome to my app!!\n")
        else:
            print("Wrong Password\n")

    def Logout(self):
        print("You're successfully log out. Thank you for using me")                                       

App = Application()
status = False

while True:
    print("User Testing Application\n1. Login\n2. Logout")
    pilih = int(input("Choose Menu? : "))
    
    if (pilih == 1):
        username = input("Username : ")
        pw = input("Password : ")
        App.Login(username,pw)
        status = True
    elif (pilih == 2) and (status == False):
        print("!!Login First!!\n")
    elif (pilih == 2) and (status == True):
        App.Logout()
        break
    else:
        print("!!No Option!!\n")
        





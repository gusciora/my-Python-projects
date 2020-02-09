import json
import getpass


def new_acc(login_):
    dic = json.load(open('credentials.txt', 'r'))
    while login_ in dic.keys():
        print("This login is already taken.")
        login_ = str(input("New login: "))
    else:
        password_ = getpass.getpass("Enter the password: ")
        password2 = getpass.getpass("Confirm the password: ")
        if password_ == password2:
            dic[login_] = password_
            json.dump(dic, open('credentials.txt', 'w'))
            print("Your accont has been created!")
        else:
            print("Passwords don't match. Please try again.")

    

def login(login_):
    dic = json.load(open('credentials.txt', 'r'))
    if login_ in dic.keys():
        password_ = getpass.getpass("Please enter your password: ")
        if password_ == dic.get(login_):
            print("You have successfully logged in.")
        else:
            print("Password is incorrect.")
    else:
        print("Such login doesn't exist.")
    
def decision():
    a = str(input("Do you want to log in (1) or create a new account (2)? Please enter '1' or '2': "))
    if a == "1":
        login_ = input("Please enter your login: ")
        login(login_)
    elif a == "2":
        login_ = input("Choose a login for a new account: ")
        new_acc(login_)
    else:
        x = input("\nEnter '1' if you want to log in or '2' if you want to create a new account. Press 'q' if you want to quit.\n")
        if x == "1":
            login_ = input("Please enter your login: ")
            login(login_)
        elif x == "2":
            login_ = input("Choose a login for a new account: ")
            new_acc(login_)
        elif x == "q" or x == "Q":
            return
        else:
            decision()

decision()
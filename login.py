import json


def new_acc(login_):
    dic = json.load(open('credentials.txt', 'r'))
    while login_ in dic.keys():
        print("This login is already taken.")
        login_ = str(input("New login: "))
    else:
        password_ = input("Enter the password: ")
        dic[login_] = password_
    json.dump(dic, open('credentials.txt', 'w'))
    print("Your accont has been created!")

def login(login_):
    dic = json.load(open('credentials.txt', 'r'))
    if login_ in dic.keys():
        password_ = input("Please enter your password: ")
        if password_ == dic.get(login_):
            print("You have successfully log in.")
        else:
            print("Password is incorrect.")
    else:
        print("Such login doesn't exist.")
    
def decision():
    a = str(input("Do you want to log in (1) or create a new account (2)? Please enter '1' or '2': "))
    if a == "1":
        login_ = input("Please enter your login: ")
        #password_ = input("Please enter your password: ")
        login(login_)
    elif a == "2":
        login_ = input("Choose a login for a new account: ")
        new_acc(login_)
    else:
        x = input("\nEnter '1' if you want to log in or '2' if you want to create a new account. Press 'q' if you want to quit.\n")
        if x == "q" or x == "Q":
            return
        else:
            decision()

decision()



#print(new_acc("arekk","123"))
# with open("credentials.txt", "r") as db:
#     dic = eval(db.read())
#     print(dic)
#     print(type(dic))
#     login = str(input("Enter your login: "))
#     password = str(input("Enter your passowrd: "))

#     if login in dic.keys():
#         if password == dic.get(login):
#             print("You have successfully logged in.")
#         else:
#             print("Password is incorrect.")


"""with open("credentials.txt", "w") as db:
    login = input("Enter your login: ")
    password = input("Enter your passowrd: ")

    dic[login] = password
    print(dic)

    db.write(str(dic))
    db.close()"""
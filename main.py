import getpass

database = {"king": "126542", "gypsy": "837861"}
username = input("enter your name : ")
password = getpass.getpass("enter your password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("enter password again : ")
            break
print("Verified")

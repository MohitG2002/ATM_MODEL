import json


# ------------------- ADDING USER DATA ----------------------

# user_data = {
#     f"{input('enter your username:').lower()}": {
#         "password": f"{input('enter your password:')}",
#         "transaction_h": [],
#     }
# }
#
# print(user_data)
#
# with open("data.json", "w") as data:
#     json.dump(user_data, data, indent=4)
    # database = json.load(data)
    # database.update(user_data)
    # with open("data.json", "w") as datanew:
    #     json.dump(database, datanew, indent=4)


# ---------------------- ATM FUNCTIONALITY ----------------------------- #

atm_is_on = True

while atm_is_on:
    ask = input("Do you want to make a new transaction? (Y/N): ").lower()
    if ask == "y":
        with open("data.json", "r") as data:
            database = json.load(data)

            user_id = input("enter your user name? ").lower()

            if user_id in database:
                password = input("enter your password:")
                if password == database[user_id]["password"]:
                    transaction = input("choose from following options:\n 1(Transaction History)/2(Withdraw)/3("
                                        "Deposit)/4(Transfer)/0(Quit):")
                    if transaction == "1":
                        print(database[user_id]["transaction_h"])
                    elif transaction == "2":
                        amount = int(input("enter the amount:"))
                        database[user_id]["transaction_h"].append(f"{amount} withdrawn")
                        with open("data.json", "w") as datanew:
                            json.dump(database, datanew, indent=4)
                    elif transaction == "3":
                        amount = int(input("enter the amount:"))
                        database[user_id]["transaction_h"].append(f"{amount} deposited")
                        with open("data.json", "w") as datanew:
                            json.dump(database, datanew, indent=4)
                    elif transaction == "4":
                        amount = int(input("enter the amount:"))
                        database[user_id]["transaction_h"].append(f"{amount} transferred")
                        with open("data.json", "w") as datanew:
                            json.dump(database, datanew, indent=4)
                    elif transaction == "0":
                        print("Thank You!")
                        atm_is_on = False
                    else:
                        print("Sorry1 invalid entry")
                else:
                    print("invalid password")
            else:
                print("invalid user id")

    else:
        print("Thank You!")
        atm_is_on = False

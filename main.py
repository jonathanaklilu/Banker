import random
from datetime import datetime


class Creating_bank_user:



    def creating_login(self):
        self.username = input("Enter your Username: ")
        self.password = input("Enter your Password: ")
        self.first_name = input("Enter your First Name: ")
        self.last_name = input("Enter your Last Name: ")
        self.id = ''
        self.pin = ''
        for i in range(3):
            self.id += random.choice(self.username)
            self.pin += random.choice("123456789")
        print("Welcome to your Bank Account")
        print("This is your following information")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}\nPassword: {self.password}\n")
        print("REMEMBER YOUR ID AND PIN")
        print(f"ID: {self.id} | Pin: {self.pin}\n")
        with open('bank_userids.txt', 'a') as userids:
            userids.write(self.id + '\n')
            userids.close()
        with open('bank_userpins.txt', 'a') as userpins:
            userpins.write(self.pin + '\n')
            userpins.close()
        with open('bank_usernames.txt', 'a') as usernames:
            usernames.write(self.username + '\n')
            usernames.close()
        with open('bank_password.txt', 'a') as passwords:
            passwords.write(self.password + '\n')
            passwords.close()
        with open('bank_first_name.txt', 'a') as firstnames:
            firstnames.write(self.first_name + '\n')
            firstnames.close()
        with open('bank_last_name.txt', 'a') as lastnames:
            lastnames.write(self.last_name + '\n')
            lastnames.close()
        with open('withdraw_nums.txt', 'a') as withdraw_nums:
            withdraw_nums.write(f"0\n")
            withdraw_nums.close()
        with open('withdraw_ids.txt', 'a') as withdraw_ids:
            withdraw_ids.write(f"{self.id}\n")
            withdraw_ids.close()
        with open('withdraw_data.txt', 'a') as withdraw_data:
            withdraw_data.write(f"{self.id}, 0, {self.time_stamp()}\n")
            withdraw_data.close()
        with open('deposit_nums.txt', 'a') as deposit_nums:
            deposit_nums.write(f"0\n")
            deposit_nums.close()
        with open('deposit_ids.txt', 'a') as deposit_ids:
            deposit_ids.write(f"{self.id}\n")
            deposit_ids.close()
        with open('deposit_data.txt', 'a') as deposit_data:
            deposit_data.write(f"{self.id}, 0, {self.time_stamp()}\n")
            deposit_data.close()

    def login(self):
        print(f"Welcome Back\nLogin Below ↓                                      {self.time_stamp()}\n")
        soft_username = input("Enter your username: ")
        soft_password = input("Enter your password: ")
        with open('bank_usernames.txt', 'r') as usernames:
            username_contents = usernames.readlines()
        with open('bank_password.txt', 'r') as passwords:
            passwords_contents = passwords.readlines()
        username_contents = [x.strip() for x in username_contents]
        passwords_contents =  [x.strip() for x in passwords_contents]
        name_contents = dict(zip(username_contents, passwords_contents))
        usernames.close()
        passwords.close()
        if (soft_username, soft_password) in name_contents.items():
            print("Welcome to your Bank.")
            self.welcome_page()
        else:
            print("You have one more chance to login.")
            soft_username = input("Enter your username: ")
            soft_password = input("Enter your password: ")
            with open('bank_usernames.txt', 'r') as usernames:
                username_contents = usernames.readlines()
            with open('bank_password.txt', 'r') as passwords:
                passwords_contents = passwords.readlines()
            username_contents = [x.strip() for x in username_contents]
            passwords_contents = [x.strip() for x in passwords_contents]
            name_contents = dict(zip(username_contents, passwords_contents))
            usernames.close()
            passwords.close()
            if (soft_username, soft_password) in name_contents.items():
                print("Welcome to your Bank.")
                self.welcome_page()
            else:
                print("The information you provided is Invalid.\nGoodbye")
                quit()

    def welcome_page(self):
        print(f"\nWhat would you like to do today.                {self.time_stamp()}\n")
        print("Withdraw (W,w) | Deposit (D, d) | Check Balance (C, c) | More (M/m) | Quit (Q/q)")
        made_decision = 0
        while made_decision != 'q':
            made_decision = input("What is your decision? ").lower()
            if made_decision == 'd':
                self.deposit()
            elif made_decision == 'w':
                self.withdraw()
            elif made_decision == 'c':
                self.checkbalance()
            elif made_decision == 'm':
                self.secondpage()
            elif made_decision == 'q':
                quit()

    def secondpage(self):
        print(f"\nSecond Page                                    {self.time_stamp()}")
        print("Data Logs (D/d) | Setting (S/s) | Interest Calculator (C\c) | Homepage (H/h) | Quit (Q/q)")
        made_decision = input("What is your decision? ").lower()
        while made_decision != 'q':
            if made_decision == 'd':
                self.data_log()
            elif made_decision == 's':
                self.settings()
            elif made_decision == 'c':
                self.which_calculator()
            elif made_decision == 'h':
                self.welcome_page()
            elif made_decision == 'q':
                quit()



    def soft_security_check(self):
        print("\nThis is a soft security check, you have only 1 chance to login.")
        softid = input("Enter your User ID: ")
        softpin = input("Enter your User Pin: ")
        with open('bank_userids.txt', 'r') as userids:
            userids_contents = userids.readlines()
        with open('bank_userpins.txt', 'r') as userpins:
            userpins_contents = userpins.readlines()
        userids_contents = [x.strip() for x in userids_contents]
        userpins_contents = [x.strip() for x in userpins_contents]
        user_contents = dict(zip(userids_contents, userpins_contents))
        userids.close()
        userpins.close()
        if (softid, softpin) in user_contents.items():
            print("Retrieving Information....\n")
            return softid, softpin
        else:
            print("The information you provided is Invalid.\nGoodbye")
            quit()


    def time_stamp(self):
        time = datetime.now()
        time_returner = str(time.date()) + ', ' + str(time.today().strftime("%I:%M %p"))
        return time_returner




    def deposit(self):
        softid, softpin = self.soft_security_check()
        num_deposit = int(input("Deposit Amount: "))
        if num_deposit > 0:
            with open('deposit_nums.txt', 'a') as deposit_nums:
                deposit_nums.write(f"{num_deposit}\n")
                deposit_nums.close()
            with open('deposit_ids.txt', 'a') as deposit_ids:
                deposit_ids.write(f"{softid}\n")
                deposit_ids.close()
            with open('deposit_data.txt', 'a') as deposit_data:
                deposit_data.write(f"{softid}, {num_deposit}, {self.time_stamp()}\n")
                deposit_data.close()
        else:
            print("You can not deposit a negative amount or 0")
            self.welcome_page()
        print(self.softcheckbalance(softid))
        another_deposit = input("\nDo you want to make another deposit? (Y/y) (N/n): ").lower()
        if another_deposit == 'y':
            self.deposit()
        elif another_deposit == 'n':
            self.welcome_page()
        else:
            print("Wrong Choice")
            print("Logging out...")
            quit()

    def withdraw(self):
        softid, softpin = self.soft_security_check()
        num_withdraw = int(input("Withdraw Amount: "))
        if num_withdraw > 0:
            with open('withdraw_nums.txt', 'a') as withdraw_nums:
                withdraw_nums.write(f"{num_withdraw}\n")
                withdraw_nums.close()
            with open('withdraw_ids.txt', 'a') as withdraw_ids:
                withdraw_ids.write(f"{softid}\n")
                withdraw_ids.close()
            with open('withdraw_data.txt', 'a') as withdraw_data:
                withdraw_data.write(f"{softid}, {num_withdraw}, {self.time_stamp()}\n")
                withdraw_data.close()
        else:
            print("You can not withdraw a negative number or 0")
            self.welcome_page()
        print(self.softcheckbalance(softid))
        another_withdraw = input("\nDo you want to make another withdraw? (Y/y) (N/n): ").lower()
        if another_withdraw == 'y':
            self.withdraw()
        elif another_withdraw == 'n':
            self.welcome_page()
        else:
            print("Wrong Choice")
            print("Logging out...")
            quit()

    def checkbalance(self):
        softid, softpin = self.soft_security_check()
        with open('deposit_nums.txt', 'r') as deposit_nums:
            deposit_nums_contents = deposit_nums.readlines()
        with open('deposit_ids.txt', 'r') as deposit_ids:
            deposit_ids_contents = deposit_ids.readlines()

        deposit_nums_contents = [x.strip() for x in deposit_nums_contents]
        deposit_ids_contents = [x.strip() for x in deposit_ids_contents]
        deposit_contents = tuple(zip(deposit_ids_contents, deposit_nums_contents))
        deposit_nums.close()
        deposit_ids.close()

        with open('withdraw_nums.txt', 'r') as withdraw_nums:
            withdraw_nums_contents = withdraw_nums.readlines()
        with open('withdraw_ids.txt', 'r') as withdraw_ids:
            withdraw_ids_contents = withdraw_ids.readlines()

        withdraw_nums_contents = [x.strip() for x in withdraw_nums_contents]
        withdraw_ids_contents = [x.strip() for x in withdraw_ids_contents]
        withdraw_contents = tuple(zip(withdraw_ids_contents, withdraw_nums_contents))
        withdraw_nums.close()
        withdraw_ids.close()


        total_deposit = 0
        total_withdraw = 0

        for soft_id in withdraw_contents:
            if soft_id[0] == softid:
                total_withdraw += int(soft_id[1])
        for soft_id in deposit_contents:
            if soft_id[0] == softid:
                total_deposit += int(soft_id[1])
        total_amount = total_deposit - total_withdraw
        if total_amount >= 0:
            print(f"ACCOUNT BALANCE: ${total_amount}, {self.time_stamp()}\n")
            self.welcome_page()
        else:
            print(f"ACCOUNT BALANCE: ${total_amount}, you are now in debt, {self.time_stamp()}\n")
            self.welcome_page()

    def softcheckbalance(self, input_id):
        with open('deposit_nums.txt', 'r') as deposit_nums:
            deposit_nums_contents = deposit_nums.readlines()
        with open('deposit_ids.txt', 'r') as deposit_ids:
            deposit_ids_contents = deposit_ids.readlines()

        deposit_nums_contents = [x.strip() for x in deposit_nums_contents]
        deposit_ids_contents = [x.strip() for x in deposit_ids_contents]
        deposit_contents = tuple(zip(deposit_ids_contents, deposit_nums_contents))
        deposit_nums.close()
        deposit_ids.close()

        with open('withdraw_nums.txt', 'r') as withdraw_nums:
            withdraw_nums_contents = withdraw_nums.readlines()
        with open('withdraw_ids.txt', 'r') as withdraw_ids:
            withdraw_ids_contents = withdraw_ids.readlines()

        withdraw_nums_contents = [x.strip() for x in withdraw_nums_contents]
        withdraw_ids_contents = [x.strip() for x in withdraw_ids_contents]
        withdraw_contents = tuple(zip(withdraw_ids_contents, withdraw_nums_contents))
        withdraw_nums.close()
        withdraw_ids.close()

        total_deposit = 0
        total_withdraw = 0

        for soft_id in withdraw_contents:
            if soft_id[0] == input_id:
                total_withdraw += int(soft_id[1])
        for soft_id in deposit_contents:
            if soft_id[0] == input_id:
                total_deposit += int(soft_id[1])
        total_amount = total_deposit - total_withdraw
        if total_amount >= 0:
            return f"ACCOUNT BALANCE: ${total_amount}, {self.time_stamp()}\n"
        else:
            return f"ACCOUNT BALANCE: ${total_amount}, you are now in debt, {self.time_stamp()}\n"

    def data_log(self):
        softid, softpin = self.soft_security_check()
        deposit_data_list = []
        withdraw_data_list = []
        with open('deposit_data.txt', 'r') as deposit_data:
            deposit_contents = deposit_data.readlines()
            for line in deposit_contents:
                line = line.strip('\n')
                line = line.split(', ')
                deposit_data_list.append(line)
        deposit_data.close()

        firstname, lastname = self.name_getter(softid)

        print(f"Data Log for {firstname.capitalize()} {lastname.capitalize()}")

        print("Deposit Information")
        print(" Amount     Date       Time")
        for semi_lst in deposit_data_list:
            if semi_lst[0] == softid:
                print(f"+{semi_lst[1]}     {semi_lst[2]}    {semi_lst[3]}")


        with open('withdraw_data.txt', 'r') as withdraw_data:
            withdraw_contents = withdraw_data.readlines()
            for line in withdraw_contents:
                line = line.strip('\n')
                line = line.split(', ')
                withdraw_data_list.append(line)
        withdraw_data.close()
        print("\nWithdraw Information")
        print(" Amount     Date       Time")
        for semi_lst in withdraw_data_list:
            if semi_lst[0] == softid:
                print(f"-{semi_lst[1]}     {semi_lst[2]}    {semi_lst[3]}")
        print(self.softcheckbalance(softid))
        self.secondpage()

    def name_getter(self, input_id):
        with open('bank_first_name.txt', 'r') as firstnames:
            first_name_contents = firstnames.readlines()
        with open('bank_userids.txt', 'r') as bank_userids:
            bank_userids_contents = bank_userids.readlines()
        with open('bank_last_name.txt', 'r') as lastnames:
            last_name_contents = lastnames.readlines()

        first_name_contents = [x.strip() for x in first_name_contents]
        bank_userids_contents = [x.strip() for x in bank_userids_contents]
        bank_first_names = tuple(zip(bank_userids_contents, first_name_contents))
        last_name_contents = [x.strip() for x in last_name_contents]
        bank_last_names = tuple(zip(bank_userids_contents, last_name_contents))

        firstnames.close()
        bank_userids.close()
        lastnames.close()



        first_name = 0
        last_name = 0

        for semi_list in bank_first_names:
            if semi_list[0] == input_id:
                first_name = semi_list[1]
        for semi_list in bank_last_names:
            if semi_list[0] == input_id:
                last_name = semi_list[1]
        return first_name, last_name


    def user_pass_getter(self, input_id):
        with open('bank_usernames.txt', 'r') as usernames:
            username_contents = usernames.readlines()
        with open('bank_userids.txt', 'r') as bank_userids:
            bank_userids_contents = bank_userids.readlines()
        with open('bank_password.txt', 'r') as passwords:
            password_contents = passwords.readlines()

        username_contents = [x.strip() for x in username_contents]
        bank_userids_contents = [x.strip() for x in bank_userids_contents]
        bank_usernames_id = tuple(zip(bank_userids_contents, username_contents))
        password_contents = [x.strip() for x in password_contents]
        bank_passwords_id = tuple(zip(bank_userids_contents, password_contents))

        usernames.close()
        bank_userids.close()
        passwords.close()


        username = 0
        password = 0

        for semi_list in bank_usernames_id:
            if semi_list[0] == input_id:
                username = semi_list[1]
        for semi_list in bank_passwords_id:
            if semi_list[0] == input_id:
                password = semi_list[1]
        return username, password

    def account_creation_date(self, input_id):
        with open('withdraw_data.txt', 'r') as withdraw_nums:
            withdraw_nums_contents = withdraw_nums.readlines()
        with open('withdraw_ids.txt', 'r') as withdraw_ids:
            withdraw_ids_contents = withdraw_ids.readlines()

        withdraw_nums_contents = [x.strip() for x in withdraw_nums_contents]
        withdraw_ids_contents = [x.strip() for x in withdraw_ids_contents]
        withdraw_contents = tuple(zip(withdraw_ids_contents, withdraw_nums_contents))
        withdraw_nums.close()
        withdraw_ids.close()
        first_list = []
        for semi_tuple in withdraw_contents:
            if semi_tuple[0] == input_id:
                first_list.append(semi_tuple[1].split(', '))
                break
        date = first_list[0][2]
        time = first_list[0][3]
        return date, time

    def settings(self):
        softid, softpin = self.soft_security_check()
        username, password = self.user_pass_getter(softid)
        print("\nSettings")
        print("\nAccount Information")
        print(f"Your username is: {username}")
        print(f"Your password is: {password}")
        print(f"Your user ID is: {softid}")
        print(f"Your user Pin is: {softpin}")
        date, time = self.account_creation_date(softid)
        print(f"Date account created: {date}, {time}")
        self.secondpage()

    def which_calculator(self):
        print("What type of interest would you like to calculate.")
        made_decision = input("Simple or Compound Interest (S\s) (C/c): ").lower()
        if made_decision == 's':
            self.simple()
        elif made_decision == 'c':
            self.compound()
        else:
            print("Wrong choice, you are being redirected to the Home Page\n")
            self.welcome_page()

    def compound(self):
        print("Compound Interest Calculater")
        p = int(input("Enter your starting number: "))
        n = int(input("Enter how many compounding periods per year: "))
        r = float(input("Enter your annual interest (Ex. 13% = 13): "))
        y = int(input("Enter the amount of years"))
        money = p * ((1 + ((r/100)/n)) ** (n*y))
        money = round(money, 2)
        print(f"Total after {y} years is ${money}\n")
        made_decision = input("Do want to make another calculation? (Y/y) (N/n): ").lower()
        if made_decision == 'y':
            self.which_calculator()
        elif made_decision == 'n':
            print("Being redirected to the Second Page")
            self.secondpage()
        else:
            print("Invalid Input\n Being redirected to the Home page")
            self.welcome_page()

    def simple(self):
        print("\n Simple Interest Calculator")
        p = int(input("Enter your starting number: "))
        r = float(input("Enter your annual interest (Ex. 13% = 13): "))
        n = input("Would you like to calculate the interest over, months or years? (M\m) (Y\y): ").lower()
        if n == 'm':
            t = int(input("Enter the amount of months: "))
            money = (p*(r/100)*(t/12))
            total = money + p
            print(f"Total after {t} months is ${round(total, 2)} ")
        elif n == 'y':
            t = int(input("Enter the amount of years: "))
            money = (p*(r/100)*t)
            total = money + p
            print(f"Total after {t} years is ${round(total, 2)} ")
        else:
            print("Invalid Input\n Being redirected to the Home page")
            self.welcome_page()
        made_decision = input("Do want to make another calculation? (Y/y) (N/n): ").lower()
        if made_decision == 'y':
            self.which_calculator()
        elif made_decision == 'n':
            print("Being redirected to the Second Page")
            self.secondpage()
        else:
            print("Invalid Input\n Being redirected to the Home page")
            self.welcome_page()


New_bank = Creating_bank_user()

print("Welcome to your Bank.")
decision = input("Would you like to Login or Create an Account? (L/l) (C/c): ").lower()
if decision == 'l':
    New_bank.login()
elif decision == 'c':
    New_bank.creating_login()
    New_bank.login()
else:
    print("Invalid decision, You have more chance for a correct input\n")
    decision = input("Would you like to Login or Create an Account? (L/l) (C/c): ").lower()
    if decision == 'l':
        New_bank.login()
    elif decision == 'c':
        New_bank.creating_login()
    else:
        quit()





#tan #363

# jonathan password
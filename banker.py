from main import Creating_bank_user


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


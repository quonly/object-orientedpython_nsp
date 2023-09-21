from Bank import *

print(Bank())
oBank = Bank()
print(oBank)

joesAccountNumber = oBank.createAccount('Joe', 100, 'JoesPassword')
print("joe's account number is:", joesAccountNumber)

mos = oBank.createAccount('Mos', 500, 'mos')
print("mos's account number is:", mos)

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To open a new account press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w ')
    print()

    action = input('What do you wnat to do? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        oBank.balance()

    elif action == 'c':
        oBank.closeAccount()

    elif action == 'd':
        oBank.deposit()

    elif action == 's':
        oBank.show()

    elif action == 'q':
        break

    elif action == 'w':
        oBank.withdraw()

    else:
        print('Sorry, that was not a valid action. Please try again.')

print('Done')


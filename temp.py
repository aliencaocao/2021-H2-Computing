balance = 1000.00

def deposit(amt):
    global balance
    balance += amt
    print(f'Deposited ${amt}, new balance is ${balance:.2f}.')
    return 0

def withdraw():
    global balance
    print('You can withdraw the following amount:\n1. $50\n2. $100\n3. $200\n4. $500\n5. Back\nPlease input your choice below: ')
    withdrawChoice = int(input('Withdrawal Choice (1-5)； '))
    if withdrawChoice == 1:
        if balance < 50:
            print(f'Your bank balance is ${balance:.2f}, which is lower than the minimum withdrawal amount of $50.')
            return 1
        else:
            balance -= 50
            print(f'Withdrawal success. New balance: ${balance:.2f}.')
    elif withdrawChoice == 2:
        if balance < 100:
            print(f'Your bank balance is ${balance:.2f}, which is lower than the amount requested to withdraw ($100).')
            return 1
        else:
            balance -= 100
            print(f'Withdrawal success. New balance: ${balance:.2f}.')
            return 0
    elif withdrawChoice == 3:
        if balance < 200:
            print(f'Your bank balance is ${balance:.2f}, which is lower than the amount requested to withdraw ($200).')
            return 1
        else:
            balance -= 200
            print(f'Withdrawal success. New balance: ${balance:.2f}.')
            return 0
    elif withdrawChoice == 4:
        if balance < 500:
            print(f'Your bank balance is ${balance:.2f}, which is lower than the amount requested to withdraw ($500).')
            return 1
        else:
            balance -= 500
            print(f'Withdrawal success. New balance: ${balance:.2f}.')
            return 0
    elif withdrawChoice == 5:
        return 0
    else:
        print('Please enter a valid choice.')
        return 1

def seeBalance():
    global balance
    print(f'The balance is ${balance:.2f}')

def quit():
    print('Thanks and have a great day!')

def main():
    print('Welcome to ATM!')
    while True:
        print('\n1. Deposit\n2. Withdrawal\n3. See balance\n4. Quit\n')
        choice = int(input('Select the task (1-4): '))
        if choice == 1:
            deposit(float(input('Enter the amount to deposit: ')))
        elif choice == 2:
            success = withdraw()
            if success == 0:  # 0 means success, 1 means error. If error, keep retrying in withdraw function
                continue
            else:
                withdraw()
        elif choice == 3:
            seeBalance()
        elif choice == 4:
            quit()
            break
        else:
            print('Please input an integer from 1 to 4')

main()

balance = 49.9


def deposit(amt):
    global balance
    balance += amt
    print(f'Deposited ${amt}, new balance is ${balance:.2f}.')
    return 0


def withdraw():
    global balance
    if balance < 50:
        print(f'Your bank balance is ${balance:.2f}, which is lower than the minimum withdrawal amount of $50.')
        return 1
    else:
        print()
        print(
            'You can with draw the following amount:\n1. $50\n2. $100\n3. $200\n4. $500\n5. Back\nPlease input your choice below: ')
        withdrawChoice = int(input('Withdrawal Choice (1-5)； '))
        if withdrawChoice == 1:
            balance -= 50
            print(f'Withdrawal success. New balance: ${balance:.2f}.')
        elif withdrawChoice == 2:
            if balance < 100:
                print(f'Your bank balance is ${balance:.2f}, which is lower than the amount requested to withdraw.')
                return 1
            else:
                balance -= 100
                print(f'Withdrawal success. New balance: ${balance:.2f}.')
                return 0
        elif withdrawChoice == 3:
            if balance < 200:
                print(f'Your bank balance is ${balance:.2f}, which is lower than the amount requested to withdraw.')
                return 1
            else:
                balance -= 200
                print(f'Withdrawal success. New balance: ${balance:.2f}.')
                return 0
        elif withdrawChoice == 4:
            if balance < 500:
                print(f'Your bank balance is ${balance:.2f}, which is lower than the amount requested to withdraw.')
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
    return f'The balance is ${balance:.2f}'


def quit():
    return 'Thanks and have a great day!'


def main():
    print('Welcome to ATM!')
    while True:
        print()
        print('1. Deposit\n2. Withdrawal\n3. See balance\n4. Quit\n')
        print()
        choice = int(input('Select the task (1-4): '))
        if choice == 1:
            deposit(float(input('Enter the amount to deposit: ')))
            continue
        elif choice == 2:
            success = withdraw()
            if success == 0:
                continue
        elif choice == 3:
            print(seeBalance())
            continue
        elif choice == 4:
            print(quit())
            break
        else:
            print('Please input an integer from 1 to 4')
            continue


main()

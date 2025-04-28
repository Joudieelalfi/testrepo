def show_balance(balance):
    print(f'your balance is ${balance:.2f}')

def deposit():
    print("***************************")
    amount = float(input("enter an amount to be deposited"))
    print("***************************")
    if amount < 0:
        print("***************************")
        print("that is not a valid amount")
        print("***************************")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input('enter amount to be withdrawn'))
    if amount > balance:
        print('Insufficient funds.')
        return 0
    elif amount < 0:
        print('Amount must be greater than zero.')
        return 0
    else:
        return amount



def main():
    balance = 0
    is_running = True 

    while is_running:
        print("***************************")
        print("    Banking program      ")
        print("***************************")
        print("1. show balance")
        print("2. deposit")
        print("3.withdraw")
        print("4. exit")
        print("***************************")

        choice = input(" enter a choice from (1-4)")

        if choice == "1":
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False 
        else:
            print("***************************")
            print('Invalid choice, Try again')
            print("***************************")

    print("***************************")
    print('Thank you, have a nice day.')
    print("***************************")


if __name__ == '__main__':
    main()

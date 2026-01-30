balance = 0

def show_menu():
    print("1. Check Balance: ")
    print("2. Deposit Money: ")
    print("3. Withdraw Money:")
    print("4. Exit: ")


def deposit(balance):
    n = int(input("Enter deposit amount: "))
    if n > 0:
        balance += n
        print("Balance after deposit:", balance)
    else:
        print("Invalid deposit amount")
    return balance

def withdraw(balance):
    n = int(input("Enter the amount: "))
    if n > 0 and n <= balance:
        balance -= n
        print("Balance after withdwar: ", balance)
    else:
        print("Insuficiant balance or invalid amount!!!")
    return balance


while True:
    show_menu()

    try:
        condition = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number")
        continue
    

    if (condition == 1):
        print("Current Balance: ", balance)

    elif (condition == 2):
        balance = deposit(balance)

    elif (condition == 3):
        balance = withdraw(balance)

    elif (condition == 4):
        print("Thank you for using ATM")
        break
    
    else:
        print("Invalid Intruction!!!")
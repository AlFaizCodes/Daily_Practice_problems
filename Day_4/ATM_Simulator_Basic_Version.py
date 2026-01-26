balance = 0


while True:
    print("1. Check Balance: ")
    print("2. Deposit Money: ")
    print("3. Withdraw Money:")
    print("4. Exit: ")


    condition = int(input("Enter your choice: "))

    if (condition == 1):
        print("Current Balance: ", balance)

    elif (condition == 2):
        n = int(input("Enter deposit amount: "))
        if n > 0:
            balance += n
            print("Balance after deposit:", balance)
        else:
            print("Invalid deposit amount")
    elif (condition == 3):
        n = int(input("Enter the amount: "))
        if n > 0 and n <= balance:
            balance -= n
            print("Balance after withdwar: ", balance)
        else:
            print("Insuficiant balance or invalid amount!!!")

    elif (condition == 4):
        print("Thank you for using ATM")
        break
    
    else:
        print("Invalid Intruction!!!")


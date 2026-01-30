pin = 1234
attempts = 0
balance = 0
history = []

# ---------- PIN CHECK ----------
while attempts < 3:
    password = int(input("Enter your Password PIN: "))
    if password == pin:
        print("Access Granted\n")
        break
    else:
        attempts += 1
        print("Wrong PIN")
else:
    print("Too many wrong attempts. Account locked.")
    exit()

# ---------- FUNCTIONS ----------
def show_menu():
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

def deposit(balance):
    n = int(input("Enter deposit amount: "))
    if n > 0:
        balance += n
        history.append(f"Deposited ₹{n}")
        print("Balance after deposit:", balance)
    else:
        print("Invalid deposit amount")
    return balance

def withdraw(balance):
    n = int(input("Enter withdraw amount: "))
    if n > 0 and n <= balance:
        balance -= n
        history.append(f"Withdrawn ₹{n}")
        print("Balance after withdraw:", balance)
    else:
        print("Insufficient balance or invalid amount")
    return balance

# ---------- MAIN LOOP ----------
while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        balance = deposit(balance)

    elif choice == 3:
        balance = withdraw(balance)

    elif choice == 4:
        if not history:
            print("No transactions yet")
        else:
            print("Transaction History:")
            for item in history:
                print("-", item)

    elif choice == 5:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid Instruction")

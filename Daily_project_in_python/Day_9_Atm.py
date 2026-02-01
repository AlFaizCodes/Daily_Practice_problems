FILE_NAME = "data.txt"

def load_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()
            balance = int(lines[0].strip())
            history = []

            for line in lines[1:]:
                history.append(line.strip())

            return balance, history
    except FileNotFoundError:
        return 0, []



def save_data(balance, history):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        file.write(str(balance) + "\n")
        for item in history:
            file.write(item + "\n")



def show_menu():
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")


def deposit(balance, history):
    amount = int(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        history.append(f"Deposited ₹{amount}")
        save_data(balance, history)
        print("Deposit successful")
    else:
        print("Invalid amount")
    return balance


def withdraw(balance, history):
    amount = int(input("Enter withdraw amount: "))
    if amount > 0 and amount <= balance:
        balance -= amount
        history.append(f"Withdrawn ₹{amount}")
        save_data(balance, history)
        print("Withdraw successful")
    else:
        print("Insufficient balance")
    return balance


balance, history = load_data()

print("ATM Started")
print("Balance Loaded:", balance)

while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        balance = deposit(balance, history)

    elif choice == 3:
        balance = withdraw(balance, history)

    elif choice == 4:
        if not history:
            print("No transactions yet")
        else:
            print("Transaction History:")
            for h in history:
                print("-", h)

    elif choice == 5:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")

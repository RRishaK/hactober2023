class Bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, name, initial_balance=0):
        if name not in self.customers:
            self.customers[name] = initial_balance
            print("Account created for", name)
        else:
            print("Account already exists for", name)

    def deposit(self, name, amount):
        if name in self.customers:
            self.customers[name] += amount
            print(f"Deposited ${amount} into {name}'s account.")
        else:
            print("Account not found.")

    def withdraw(self, name, amount):
        if name in self.customers:
            if self.customers[name] >= amount:
                self.customers[name] -= amount
                print(f"Withdrew ${amount} from {name}'s account.")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    def check_balance(self, name):
        if name in self.customers:
            print(f"{name}'s account balance: ${self.customers[name]}")
        else:
            print("Account not found.")

def main():
    bank = Bank()

    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(name, initial_balance)

        elif choice == "2":
            name = input("Enter customer name: ")
            amount = float(input("Enter the deposit amount: "))
            bank.deposit(name, amount)

        elif choice == "3":
            name = input("Enter customer name: ")
            amount = float(input("Enter the withdrawal amount: "))
            bank.withdraw(name, amount)

        elif choice == "4":
            name = input("Enter customer name: ")
            bank.check_balance(name)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

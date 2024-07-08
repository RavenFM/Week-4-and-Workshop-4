# Task 1: Create the User class
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

# Task 2: Add User class instance methods
    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password

# Task 3: Create BankUser subclass
class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0.0

# Task 4: Add BankUser class instance methods
    def show_balance(self):
        print(f"{self.name} has an account balance of: ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

# Task 5: Transfer and request money
    def transfer_money(self, amount, recipient, pin):
        print(f"You are transferring ${amount} to {recipient.name}")
        print("Authentication required")
        entered_pin = input("Enter your PIN: ")
        if self.pin == int(entered_pin):
            if amount > self.balance:
                print("Insufficient funds for transfer")
                return False
            else:
                self.balance -= amount
                recipient.balance += amount
                print("Transfer authorized")
                print(f"Transferring ${amount} to {recipient.name}")
                self.balance = 0  
                return True
        else:
            print("Invalid PIN. Transaction canceled.")
            return False

    def request_money(self, amount, user, user_pin, password):
        print(f"You are requesting ${amount} from {user.name}")
        print("User authentication is required...")
        entered_pin = input(f"Enter {user.name}'s PIN: ")
        if user_pin == int(entered_pin):
            entered_password = input("Enter your password: ")
            if password == entered_password:
                if amount > user.balance:
                    print("Insufficient funds in the user's account")
                    return False
                else:
                    user.balance -= amount
                    self.balance += amount
                    print("Request authorized")
                    print(f"{user.name} sent ${amount}")
                    user.balance = 0  
                    return True
            else:
                print("Invalid password. Transaction canceled.")
                return False
        else:
            print("Invalid PIN. Transaction canceled.")
            return False


""" Driver Code for Task 1 """
# user1 = User("Bob", 1234, "password")
# print(f"Name: {user1.name}, PIN: {user1.pin}, Password: {user1.password}")

""" Driver Code for Task 2 """
# user1 = User("Bob", 1234, "password")
# print(f"Name: {user1.name}, PIN: {user1.pin}, Password: {user1.password}")
# user1.change_name("Alice")
# user1.change_pin(4321)
# user1.change_password("new_password")
# print(f"Updated Name: {user1.name}, Updated PIN: {user1.pin}, Updated Password: {user1.password}")

""" Driver Code for Task 3 """
# bank_user1 = BankUser("Charlie", 5678, "securepass")
# print(f"Name: {bank_user1.name}, PIN: {bank_user1.pin}, Password: {bank_user1.password}, Balance: {bank_user1.balance}")

""" Driver Code for Task 4 """
# bank_user1 = BankUser("Charlie", 5678, "securepass")
# bank_user1.show_balance()  
# bank_user1.deposit(1000)
# bank_user1.show_balance()  
# bank_user1.withdraw(500)
# bank_user1.show_balance()  

""" Driver Code for Task 5 """
bank_user1 = BankUser("Bob", 5678, "alicepassword")
bank_user2 = BankUser("Alice", 1234, "bobpassword")
bank_user2.deposit(5000)
print("Balances before transfer:")
bank_user1.show_balance()
bank_user2.show_balance()
if bank_user2.transfer_money(500, bank_user1, 1234):
    print("Balances after transfer:")
    bank_user1.show_balance()
    bank_user2.show_balance()
    if bank_user2.request_money(200, bank_user1, 5678, "alicepassword"):
        print("Balances after money request:")
        bank_user1.show_balance()
        bank_user2.show_balance()

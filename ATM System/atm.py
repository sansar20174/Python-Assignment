balance = 5000  

def check_balance():
    return f"\nYour current balance is: ₹{balance}\n"

def deposit(amount):
    global balance
    if amount <= 0:
        return "\n❌ Deposit amount must be greater than zero.\n"
    balance += amount
    return f"\n✅ ₹{amount} deposited successfully!\nNew Balance: ₹{balance}\n"

def withdraw(amount):
    global balance
    if amount <= 0:
        return "\n❌ Withdrawal amount must be greater than zero.\n"
    if amount > balance:
        return "\n❌ Insufficient balance!\n"
    balance -= amount
    return f"\n✅ ₹{amount} withdrawn successfully!\nRemaining Balance: ₹{balance}\n"

print("\n🏦 Welcome to Our ATM!\n")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
while True:
    print("What would you like to do?")
    print("1️⃣  Check my balance")
    print("2️⃣  Deposit money")
    print("3️⃣  Withdraw money")
    print("4️⃣  Leave")
    print("-" * 30)

    try:
        choice = int(input("Choose an option (1-4): "))

        if choice == 1:
            print(check_balance())

        elif choice == 2:
            amount = float(input("How much would you like to deposit? ₹"))
            print(deposit(amount))

        elif choice == 3:
            amount = float(input("How much would you like to withdraw? ₹"))
            print(withdraw(amount))

        elif choice == 4:
            print("\n👋 Thanks for banking with us. See you next time!\n")
            break

        else:
            print("\n⚠️  Please enter a number between 1 and 4.\n")
    
    except ValueError:
        print("\n⚠️  Please enter a valid number.\n")

class Account:
	#1 Mark for completing constructor with suitable attribute names
    def __init__(self, number, password, balance):
        self.__accountNumber = number
        self.__accountPassword = password
        self.__accountBalance = balance

	#1 Mark for returning the accountNumber attribute
    def getNumber(self):
        return self.__accountNumber
     
	#1 Mark for correctly returning either True or False
    def checkPassword(self, password):
        if password == self.__accountPassword:
            return True
        else:
            return False
    
	#1 Mark for returning the accountBalance (or equivalent) attribute    
    def getBalance(self):
        return self.__accountBalance
     
	#1 Mark for setting the accountBalance (or equivalent) attribute to the value given for newBalance
    def setBalance(self, newBalance):
        self.__accountBalance = newBalance

class Bank:
    def __init__(self):
        self.__accounts = []
        self.__latestAccount = -1 
       
	#1 Mark for returning the account number if the given account number matches the given password
	#1 Mark for returning -1 if the account number isn't found or the given password is not correct
    def login(self):
        accountNo = input("Please enter your account number: \n")
        password = input("Please enter the password for the account number " + str(accountNo) + ":\n")
        try:
            accountNo = int(accountNo)
            for account in self.__accounts:
                if account.getNumber() == accountNo and account.checkPassword(password):
                    return account.getNumber()
        except:
            pass
        print("Incorrect account number or password entered. Try again.\n")
        return -1
 
	#1 Mark for updating the given account's balance if a valid amount is given
	#1 Mark for displaying an error message if an invalid amount is given
    def deposit(self, number):
        try:
            amount = float(input("Enter the amount of money you would like to deposit:\n£")) 
        except:
            print("Invalid value given")
            amount = 0
        self.__accounts[number].setBalance(self.__accounts[number].getBalance() + amount)

	#1 Mark for updating the given account's balance if a valid amount is given
	#1 Mark for displaying an error message if an invalid amount is given
	#1 Mark for displaying a message if a higher amount is requested than the account balance contains
    def withdraw(self, number):
        try:
            amount = float(input("Enter the amount of money you would like to withdraw:\n£"))
        except:
            print("Invalid value given")
            amount = 0    
        if amount <= self.__accounts[number].getBalance():
            self.__accounts[number].setBalance(self.__accounts[number].getBalance() - amount)
        else:
            print("Your account has insufficient funds to complete this transaction.")
       
	#1 Mark for displaying the account's current balance
    def checkBalance(self, number):
        print("Your account currently contains:\n£" + str(self.__accounts[number].getBalance()) + "\n")
    
	#1 Mark for adding a new account (with accountNumber equal to the value of latestAccount) to the accounts arraylist
	#1 Mark for updating the value of latestAccount
    def addAccount(self):
        self.__latestAccount += 1
        newNumber = self.__latestAccount
        newPassword = input("Please enter a password for your new account: ")
        newBalance = 0
        account = Account(newNumber, newPassword, newBalance)
        self.__accounts.append(account)
        print("Your new account has account number " + str(account.getNumber()))
        
def main():
    bank = Bank()
    loggedIn = False
    quitting = False
    
    while not loggedIn and not quitting:
        response = input("Do you have an account? (y/n/quit)")
        if response == "y":
            account = bank.login()
            if account != -1:
                loggedIn = True
        elif response =="n":
            bank.addAccount()
        elif response =="quit":
            quitting = True
            
    while not quitting:
        option = input("Press 1 to check your balance\nPress 2 to deposit money\nPress 3 to withdraw money\nPress 4 to exit:\n")
        if option == "1":
            bank.checkBalance(account)
        elif option == "2": 
            bank.deposit(account)
            bank.checkBalance(account)
        elif option == "3":
            bank.withdraw(account)
            bank.checkBalance(account)
        elif option == "4":
            quitting = True
        else:
            print("Invalid option selected")
    
if __name__ == '__main__':
    main()
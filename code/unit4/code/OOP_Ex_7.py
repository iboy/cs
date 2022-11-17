class Account:
    def __init__(self, number, password, balance): #A new bank account should be defined with a given account number, password and balance
        self.__accountNumber = number
        self.__
        self.__

    def getNumber(self): 
    #This method should return the account number of this account
    
    def checkPassword(self, password): 
    #This method should check if a given password is equal to the password for this account
		
    def getBalance(self): 
    #This method should return the balance of this account
		
    def setBalance(self, newBalance):
	#This method should change the balance of this account to a specified new value

class Bank:
    def __init__(self): #A new bank is defined with a list of bank accounts and a value that keeps track of the account number of the most recently added account
        self.__accounts = []
        self.__latestAccount = -1 
            
    def login(self): 
    #This method should ask the user to give their account number and password, returning the account number if they match, or returning -1 if not
	
    def deposit(self, number):
	#This method should ask the user how much money they want to deposit into their account, and correctly update the balance of their account

    def withdraw(self, number):
	#This method should ask the user how much money they want to withdraw from their account, and correctly update the balance of their account
           
    def checkBalance(self, number):
	#This method should display a message telling the user how much money is in their account
        
    def addAccount(self):
	#This method should create a new account with an account number 1 larger than the account number or the last account created, a password given by the user, and a balance of 0. The account should be added to the bank's list of accounts
        
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
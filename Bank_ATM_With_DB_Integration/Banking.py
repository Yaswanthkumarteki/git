class Bank:
    Bank_type = "Public Limited"

    #static method for creating user
    @staticmethod
    def create_user(account_number,atm_number = 00000):
        user_name = input("Enter your name: ")
        mobile_number = input("Enter mobile number: ")
        branch_name = input("Enter branch name: ")
        city_name = input("Enter city name: ")
        return {"user_name":user_name,
                "account_number": account_number, 
                "mobile_number": mobile_number,
                "branch_name": branch_name, 
                "city_name":city_name, 
                "account_balance": 000000000000,
                "atm_card_number":atm_number,
                "pin": 0000}


    #initializing the customer
    def __init__(self, branch_account_number, branch_ATM_card_number = None):
        self.__account_number = branch_account_number
        if branch_ATM_card_number == None:
            self.__user_data = Bank.create_user(self.__account_number)
        else:
            self.__user_data = Bank.create_user(self.__account_number, branch_ATM_card_number)

        self.__user_name = self.__user_data.get("user_name")
        self.__account_number = self.__user_data.get("account_number")
        self.__mobile_number = self.__user_data.get("mobile_number")
        self.__branch_name = self.__user_data.get("branch_name")
        self.__city_name = self.__user_data.get("city_name")
        self.__account_balance = self.__user_data.get("account_balance")
        self.__atm_card_number = self.__user_data.get("atm_card_number")
        self.__pin = self.__user_data.get("pin")
        
        

    def get_customer_details(self):
        return {"user_name":self.__user_name, 
                "account_number": self.__account_number,
                "mobile_number": self.__mobile_number,
                "branch_name": self.__branch_name, 
                "city_name":self.__city_name, 
                "account_balance": self.__account_balance, 
                "atm_card_number":self.__atm_card_number,
                "pin":self.__pin}
    
    def get_account_balance(self):
        return self.__account_balance
    
    def set_account_balance(self, value):
        self.__account_balance += value
        
    def get_atm_card_number(self):
        return self.__atm_card_number
    def __str__(self):
        return self.__user_name

    
    
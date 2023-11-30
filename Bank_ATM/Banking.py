class Bank:
    branch_account_number = 1000000
    branch_ATM_card_number = 1000

    @staticmethod
    def create_user():
        user_name = input("Enter your name: ")
        mobile_number = input("Enter mobile number: ")
        branch_name = input("Enter branch name: ")
        city_name = input("Enter city name: ")
        account_balance = 0000000
        return {"user_name":user_name, 
                "mobile_number": mobile_number,
                "branch_name": branch_name, 
                "city_name":city_name, 
                "account_balance": account_balance}

    def __init__(self):
        Bank.branch_account_number += 1
        self.__account_number = Bank.branch_account_number
        self.__user_data = Bank.create_user()
        self.__user_name = self.__user_data.get("user_name")
        self.__mobile_number = self.__user_data.get("mobile_number")
        self.__branch_name = self.__user_data.get("branch_name")
        self.__city_name = self.__user_data.get("city_name")
        self.__account_balance = self.__user_data.get("account_balance")
        Bank.branch_ATM_card_number += 1
        self.__ATM_card_number = Bank.branch_ATM_card_number

    def get_customer_details(self):
        return {"user_name":self.__user_name, 
                "mobile_number": self.__mobile_number,
                "branch_name": self.__branch_name, 
                "city_name":self.__city_name, 
                "account_balance": self.__account_balance, 
                "atm_card_number":self.__ATM_card_number}
    
    def get_account_balance(self):
        return self.__account_balance
    
    def set_account_balance(self, value):
        self.__account_balance += value
        
    def get_atm_card_number(self):
        return self.__ATM_card_number
    def __str__(self):
        return self.__user_name
    
if __name__ == "__main__":
    c1 = Bank()
    print(c1)
    
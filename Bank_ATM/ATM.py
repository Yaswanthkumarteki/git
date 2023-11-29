from Banking import Bank

class Incorrect_PIN(Exception):
    def __init__(self):
        self.error = "You have entered a wrong PIN...! \nPlease enter correct PIN"

class Invalid_Input(Exception):
    def __init__(self):
        self.error = "You have entered a input...! \nPlease enter correct input"

class Insufficient_balance(Exception):
    def __init__(self):
        self.error = "You don't have sufficient balance"



class ATM(Bank):
    @staticmethod
    def set_atm_pin():
        try:
            pin = input("please enter a 4 digits pin to set: ")
            if type(pin) != int or len(str(pin)) != 4:
                raise Invalid_Input
            else:
                pin = int(pin)
                return pin
        except Exception as ex:
            if isinstance(ex,Invalid_Input):
                return ex.error
        
    
    def __init__(self, bank_customer):
        self.__card_number = bank_customer.get_atm_card_number()
        self.__atm_pin = ATM.set_atm_pin()
        self.__instance = bank_customer

    def change_pin(self):

        try:
            old_pin = input("please enter your existing PIN: ")
            if type(old_pin) != int or len(str(old_pin)) != 4:
                raise Invalid_Input
            else:
                old_pin = int(old_pin)
                if self.__atm_pin == old_pin:
                    new_pin = input("Please enter a new pin to set")
                    if type(new_pin) != int or len(str(new_pin) != 4):
                        raise Invalid_Input
                    else:
                        self.__atm_pin = new_pin
                else:
                    raise Incorrect_PIN
        except Exception as ex:
            if isinstance(ex,Invalid_Input):
                return ex.error
            elif isinstance(ex,Incorrect_PIN):
                return ex.error
            else:
                raise Exception ("Some Thing went wrong....!")
        
    def deposit_money(self):
        amount = input("please enter the amount you want to deposit in INR: ")
        self.__instance.set_account_balance(amount)
        self.show_current_balance()

    def withdraw_money(self):
        withdraw_amount = int(input("Please enter the amount you want to withdraw in INR "))
        if withdraw_amount > self.__instance.set_account_balance():
            raise Insufficient_balance
        else:
            self.__instance.set_account_balance(-withdraw_amount)

    def show_current_balance(self):
        self.__instance.get_account_balance()
    
    def insert_atm_card(self):
        pin = input("Please Enter your PIN: ")
        try:
            if type(pin) != int or len(str(pin)) != 4:
                raise Invalid_Input
            else:
                if self.__atm_pin == int(pin):
                    user_option = input(" Please select the option \n1.change PIN \n2.view balance \n3.deposit money \n4.withdraw money")
                    if type(user_option) == int:
                        if user_option < 1 or user_option>4:
                            raise Invalid_Input
                        else:
                            match user_option:
                                case 1:
                                    return self.change_pin()
                                case 2:
                                    return self.show_current_balance()
                                case 3:
                                    return self.deposit_money()
                                case 4:
                                    return self.withdraw_money()
                    else:
                            raise Invalid_Input
                else:
                    raise Incorrect_PIN

        except Exception as ex:
            if isinstance(ex,Invalid_Input):
                return ex.error
            elif isinstance(ex,Incorrect_PIN):
                return ex.error
            else:
                raise Exception ("Some Thing went wrong....!")
            

# if __name__ == "__main__":
#     c1 = Bank()


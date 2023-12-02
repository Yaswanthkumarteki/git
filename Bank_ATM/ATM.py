from Banking import Bank

class Incorrect_PIN(Exception):
    def __init__(self):
        self.error = "You have entered a wrong PIN...! Please enter correct PIN"

class Invalid_Input(Exception):
    def __init__(self):
        self.error = "You have entered an invalid input...! Please enter correct input"

class Insufficient_balance(Exception):
    def __init__(self):
        self.error = "You don't have sufficient balance"



class ATM(Bank):

    @staticmethod
    def validate_set_PIN():
        try:
            try:
                pin = int(input("please enter a 4 digits pin to set: "))
                if len(str(pin)) != 4:
                    raise Invalid_Input
            except Exception:
                raise Invalid_Input
        except Exception as ex:
            if isinstance(ex,Invalid_Input):
                raise Exception (ex.error)
            else:
                raise Exception ("Something went wrong....!")
        return pin
    

    @classmethod
    def validate_your_PIN(cls):
        try:
            try:
                pin = int(input("please enter your current 4 digits pin: "))
                if len(str(pin)) != 4:
                    raise Invalid_Input
            except Exception:
                raise Invalid_Input
        except Exception as ex:
            if isinstance(ex,Invalid_Input):
                raise Exception (ex.error)
            else:
                raise Exception ("Something went wrong....!")
        return pin
            
    def __init__(self, bank_customer):
        self.__card_number = bank_customer.get_atm_card_number()
        self.__atm_pin = ATM.validate_set_PIN()
        self.__instance = bank_customer

    def __change_pin(self):

        try:
            old_pin = ATM.validate_your_PIN()
            
            #checking if the pin is matching with old pin
            if self.__atm_pin == old_pin:
                new_pin = ATM.validate_set_PIN()                
                #setting new pin
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
        
    def __deposit_money(self):
        try:
            amount = int(input("please enter the amount you want to deposit in INR: "))
        except Exception:
            raise Exception ("Enter correct value of amount")
        self.__instance.set_account_balance(amount)
        self.__instance.get_account_balance()

    def __withdraw_money(self):
        try:
            try:
                withdraw_amount = int(input("Please enter the amount you want to withdraw in INR "))
            except Exception:
                raise Exception ("Enter correct value of amount")
            if withdraw_amount > self.__instance.get_account_balance():
                raise Insufficient_balance
            else:
                self.__instance.set_account_balance(-withdraw_amount)
        except Exception as ex:
            if isinstance(ex,Invalid_Input):
                return ex.error
            elif isinstance(ex,Incorrect_PIN):
                return ex.error
            elif isinstance(ex, Insufficient_balance):
                return ex.error
            else:
                raise Exception ("Some Thing went wrong....!", str(ex))
    
    def __show_current_balance(self):
        return self.__instance.get_account_balance()
    
    def insert_atm_card(self):
        
        try:
            pin = ATM.validate_your_PIN()

            if self.__atm_pin == pin:
                try:
                    user_option = int(input(" Please select the option 1.change PIN 2.view balance 3.deposit money 4.withdraw money"))
                except Exception:
                    raise Exception ("Choose correct option by selecting values between 1 and 4")
                if type(user_option) == int:
                    if user_option < 1 or user_option>4:
                        raise Invalid_Input
                    else:
                        match user_option:
                            case 1:
                                return self.__change_pin()
                            case 2:
                                return self.__show_current_balance()
                            case 3:
                                return self.__deposit_money()
                            case 4:
                                return self.__withdraw_money()
                else:
                        raise Invalid_Input
            else:
                raise Incorrect_PIN

        except Exception as ex:
            if isinstance(ex,Invalid_Input):
                return ex.error
            elif isinstance(ex,Incorrect_PIN):
                return ex.error
            elif isinstance(ex, Insufficient_balance):
                return ex.error

            else:
                raise Exception ("Some Thing went wrong....!", str(ex))
            
            

if __name__ == "__main__":
    c1 = Bank()
    a1 = ATM(c1)
    a1.insert_atm_card()


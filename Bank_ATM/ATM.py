from Banking import Bank

class ATM(Bank):

    @staticmethod
    def set_atm_pin():
        pin = input("please enter a pin to set: ")
        return pin
    
    def __init__(self, bank_customer):
        self.__card_number = bank_customer.get_atm_card_number()
        self.__atm_pin = ATM.set_atm_pin()

    def change_pin(self):
        old_pin = input("Please enter your old pin to change: ")
        if self.__atm_pin == old_pin:
            new_pin = input("Please enter a new pin to set")
            self.__atm_pin = new_pin
        else:
            raise Exception ("You Entered Incorrect PIN")
        
    def deposit_money(self):
        pass

    def withdraw_money(self):
        pass

    def show_current_balance(self):
        pass
    

if __name__ == "__main__":
    c1 = Bank()
    a1 = ATM(c1)
    a1.change_pin()
    pass


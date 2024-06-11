import sqlite3


# Exception classes
class Incorrect_PIN(Exception):
    def __init__(self):
        self.error = "You have entered a wrong PIN...! Please enter correct PIN"

class Invalid_Input(Exception):
    def __init__(self):
        self.error = "You have entered an invalid input...! Please enter correct input"

class Insufficient_balance(Exception):
    def __init__(self):
        self.error = "You don't have sufficient balance"

# To Validate PINs
def validate_PIN():
    try:
        try:
            pin = input("please enter your current 4 digits pin: ")
            try:
                int(pin)
            except Exception:
                raise Invalid_Input
            if len(pin) != 4:
                raise Invalid_Input
        except Exception:
            raise Invalid_Input
    except Exception as ex:
        if isinstance(ex,Invalid_Input):
            raise Exception (ex.error)
        else:
            raise Exception ("Something went wrong....!")
    return pin

# Function to create bank account
def create_bank_account():
    
    bank_status = c.execute("select * from bank;")
    bank_status = bank_status.fetchone()

    if bank_status:
        branch_account_number = bank_status[0]
        branch_ATM_card_number = bank_status[1]

    else:
        branch_account_number = 10000000
        branch_ATM_card_number = 50000

    

    branch_account_number += 1
    
    c.execute("insert into bank values(:current_account_number, :current_atm_number)", 
              {"current_account_number":branch_account_number, "current_atm_number": branch_ATM_card_number})
    connection.commit()
    atm = input("Do you opt for ATM card ? 1.Yes    2.No \n")
    if str(atm)[0].lower() == 'y' or str(atm) == '1':
        customer = Bank(branch_account_number, branch_ATM_card_number)
        atm_customer = ATM(customer)
        branch_ATM_card_number += 1
        c.execute("delete from bank")
        connection.commit()
        c.execute("insert into bank values(:current_account_number, :current_atm_number)", 
              {"current_account_number":branch_account_number, "current_atm_number": branch_ATM_card_number})
        connection.commit()

    else:
        customer = Bank(branch_account_number)
    cd = customer.get_customer_details()
    c.execute("insert into customers values(:user_name, :account_number, :mobile_number, :branch_name, :city_name, :account_balance, :atm_card_number, :pin)", cd)
    connection.commit()
    connection.close()




# connection = sqlite3.connect("bankdb.db")
# c = connection.cursor()
# cp = c.execute("select * from customers;")
# print(cp.fetchall())
# cp = c.execute("select * from bank;")
# print(cp.fetchall())
try:
    connection = sqlite3.connect("bankdb.db")
    c = connection.cursor()
    create_bank_account()
    connection.commit()
finally:
    connection.close()

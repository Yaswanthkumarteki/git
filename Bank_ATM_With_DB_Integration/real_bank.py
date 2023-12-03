import sqlite3
from ATM import ATM
from Banking import Bank





def create_bank_account():
    connection = sqlite3.connect("bankdb.db")
    c = connection.cursor()
    bank_status = c.execute("select * from bank;")
    bank_status = bank_status.fetchone()

    branch_account_number = bank_status[0]
    branch_ATM_card_number = bank_status[1]

    branch_account_number += 1
    c.execute("delete from bank")
    connection.commit()
    c.execute("insert into bank values(:current_account_number, :current_atm_number)", 
              {"current_account_number":branch_account_number, "current_atm_number": branch_ATM_card_number})
    connection.commit()
    atm = input("Do you opt for ATM card ? 1.Yes    2.No \n")
    if atm == 1 or str(atm)[0].lower() == 'y' or str(atm) == '1':
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



create_bank_account()
connection = sqlite3.connect("bankdb.db")
c = connection.cursor()
cp = c.execute("select * from customers;")
print(cp.fetchall())
# cp = c.execute("select * from bank;")
# print(cp.fetchall())
connection.close()

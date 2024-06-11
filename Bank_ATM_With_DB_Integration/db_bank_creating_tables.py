import sqlite3
import os

os.chdir(os.getcwd() + '\\git\\Bank_ATM_With_DB_Integration')
# print(os.getcwd())

connection = sqlite3.connect("bankdb.db")
c = connection.cursor()
'''
try:
    c.execute("Create table customers(user_name text, account_number integer, mobile_number integer, branch_name text, city_name text, account_balance integer, atm_card_number number, pin integer)")
    c.execute("create table bank(current_account_number integer, current_atm_number integer)")
except Exception as e:
    print(e)
    pass
# cd = c.execute("select * from customers;")
# print(cd.fetchall())
c.execute("insert into bank values(:current_account_number, :current_atm_number)", {"current_account_number":1330001, "current_atm_number": 43016})
connection.commit()
c.execute("select * from bank;")
bank_status = c.fetchone()
# print(c.fetchone())
branch_account_number = bank_status[0]
branch_ATM_card_number = bank_status[1]
# c.execute("delete from customers")
print(f"branch_account_number: {branch_account_number}, branch_ATM_card_number:{branch_ATM_card_number}")
'''
c.execute("update bank set current_account_number = (:current_account_number) and current_atm_number = (:current_atm_number)", {"current_account_number":1330001, "current_atm_number": 43016})
det = c.execute('select * from bank')
print(det.fetchall())
connection.commit()
connection.close()
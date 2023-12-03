# import sqlite3

# connection = sqlite3.connect("bankdb.db")

# c = connection.cursor()

# c.execute("Create table customers(user_name text, account_number integer, mobile_number integer, branch_name text, city_name text, account_balance integer, atm_card_number number, pin integer)")
# c.execute("create table bank(current_account_number integer, current_atm_number integer)")
# cd = c.execute("select * from customers;")
# print(cd.fetchall())
# c.execute("insert into bank values(:current_account_number, :current_atm_number)", {"current_account_number":1330001, "current_atm_number": 43016})
# connection.commit()
# c.execute("select * from bank;")
# print(c.fetchone())

# c.execute("delete from customers")
# connection.commit()
# connection.close()
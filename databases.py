import sqlite3

#conn=sqlite3.connect(':memory:')  #create a connection in memory

conn=sqlite3.connect('customer.db')  #create a connection

#create a cursor
c=conn.cursor()

# #create a table
# c.execute("""CREATE TABLE customers(
# 			first_name text,
# 			last_name text,
# 			email text
# 	)""")

#insert date into the table
# c.execute("INSERT INTO customers VALUES ('Pedro', 'Goncalves', 'pgoncalves@gmail.com')")
# c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@gmail.com')")
# c.execute("INSERT INTO customers VALUES ('Doris', 'Bao', 'doris@gmail.com')")

# many_customers=[
# 					('Wes','Brown', 'wes@mal.com'), 
# 					('Step', 'Rigg', 'rigg@mail.com'),
# 					('Tina', 'Siva', 'tina@mail.com')
# 				]
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
# print('command executed successully...')

c.execute("SELECT rowid,* FROM customers WHERE last_name LIKE 'B%'")
items=c.fetchall()

for item in items:
	print(item)

#commit our connection 
conn.commit()

#close our connection
conn.close()
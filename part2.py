# wiesliam
# these should be the only imports you need
import sys
import sqlite3
from sqlite3 import Error

# write your code here
# usage should be 
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>


def list_of_customers(c, conn):
	customer_dict = {}
	c = conn.execute("SELECT Id, CompanyName FROM customer")
	for row in c:
		customer_dict[row[0]] = row[1]
	customer_dict = sorted(customer_dict.items(), key = lambda x:x[1])
	#print(customer_dict)
	print("ID\tCustomer Name")
	for customer in customer_dict:
		print(customer[0] + '\t' + customer[1])

def list_of_employees(c, conn):
	employee_dictionary = {}
	c = conn.execute("SELECT Id, FirstName, LastName FROM employee")
	for entry in c:
		employee_dictionary[entry[0]] = (entry[1] + " " + entry[2])
	print("ID\tEmployee Name")
	for Id, name in employee_dictionary.items():
		print(str(Id) + '\t' + name)

def list_of_customer_orders(c, conn, customer_id):
	customer_order_list = []
	c = conn.execute("SELECT OrderDate FROM [Order] JOIN Customer ON [Order].CustomerId = Customer.id WHERE Customer.id = ?", (customer_id,))
	for entry in c:
		customer_order_list.append(entry[0])
	print("Order dates")
	for order in customer_order_list:
		print(order)

def list_of_employee_orders(c, conn, employee_name):
	employee_order_list = []
	c = conn.execute("SELECT OrderDate FROM [Order] JOIN Employee ON [Order].EmployeeId = Employee.id WHERE Employee.LastName = ?", (employee_name,))
	for entry in c:
		employee_order_list.append(entry[0])
	print("Order dates")
	for order in employee_order_list:
		print(order)
 
 
def create_connection(db_file):
	""" create a database connection to a SQLite database """
	try:
		conn = sqlite3.connect(db_file)
		#print(sqlite3.version)
		return conn
	except Error as e:
		print(e)

 
if __name__ == '__main__':
	conn = create_connection("/Users/LiamWies/Documents/si-507-waiver-assignment-f18-wiesliam/Northwind_small.sqlite")
	c = conn.cursor
	#print(sys.argv[1])
	if(len(sys.argv)) == 2:
		#print(sys.argv)
		if sys.argv[1] == "customers":
			list_of_customers(c, conn)

		elif sys.argv[1] == "employees":
			list_of_employees(c, conn)


	if(len(sys.argv)) == 3:
		#print(sys.argv)
		if sys.argv[2].startswith("cust="):
			list_of_customer_orders(c, conn, sys.argv[2].replace("cust=", ""))
		elif sys.argv[2].startswith("emp="):
			list_of_employee_orders(c, conn, sys.argv[2].replace("emp=", ""))




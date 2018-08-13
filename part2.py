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
	c = conn.execute("SELECT Id, CompanyName from customer")
	for row in c:
		customer_dict[row[0]] = row[1]
	customer_dict = sorted(customer_dict.items(), key = lambda x:x[1])
	#print(customer_dict)
	print("ID\tCustomer Name")
	for customer in customer_dict:
		print(customer[0] + '\t' + customer[1])
 
 
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


	if(len(sys.argv)) == 3:
		print(sys.argv)

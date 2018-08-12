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

 
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()
 
if __name__ == '__main__':
    create_connection("/Users/LiamWies/Documents/si-507-waiver-assignment-f18-wiesliam/Northwind_small.sqlite")
    print(sys.argv[1])
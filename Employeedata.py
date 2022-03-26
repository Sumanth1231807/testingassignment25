import sqlite3

from prettytable import PrettyTable

connection = sqlite3.connect("employee1.db")

tablelist = connection.execute("select name from sqlite_master where type='table' and name='Employee'").fetchall()

if tablelist != []:

    print("Table already exsist")

else:
    connection.execute(''' Create Table Employee(
                id integer primary key autoincrement,
                empcode,
                empname text,
                emp_salary integer,
                designation text
)''')

print("Employee Table Created Successfully")

while True:
    print("Select an option in an given menu")
    print("1. Add Employee data")
    print("2. View all Employees")
    print("3. Exit")

    Choice = int(input("Enter your Choice"))

    if Choice == 1:
        getemployee_code = input("Enter the Employee code:")
        getemployee_name = input("Enter the Employee name:")
        getsalary = input("Enter the Employee salary:")
        getdesignation = input("Enter the Employee designation:")

        result = connection.execute("insert into Employee(empcode,empname,emp_salary,designation) values("+getemployee_code+",'"+getemployee_name+"',"+getsalary+",'"+getdesignation+"')")

        connection.commit()

        print("Employee data inserted Successfully")

    elif Choice == 2:
        result = connection.execute("select * from Employee")

        table = PrettyTable(["id","empcode","empname","emp_salary","designation"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(table)

    elif Choice == 3:
        connection.close()
        break

    else:
        print("Invalid Choice")

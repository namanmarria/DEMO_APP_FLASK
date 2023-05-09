import datetime
from cookies_a import orders
class orderlogger:
    orders_logger = orders()

    def __init__(self,customerid=None,orderid=None,product=None,units_sold=None,revenue=None,cost=None):
        self.customerid = customerid
        self.orderid = orderid
        self.product = product
        self.units_sold = units_sold
        self.revenue = revenue
        self.cost = cost
        self.date = str(datetime.datetime.today().date())

    def insert_sql_command(self):
        sql = "insert into orders values('{customerid}','{orderid}','{product}',{units_sold},'{date}',{revenue},{cost})".format_map(vars(self))
        return sql

    def update_sql_command(self):
        sql = ("update into orders values('{customerid}','{orderid}','{product}',{units_sold},'{date}',{revenue},{cost})").format_map(vars(self))
        return sql

    def delete_log(self):
        self.customerid = int(input("Enter the log id: "))
        sql = "delete from orders where customerid = {customerid}".format_map(vars(self))
        return sql

    def get_all_logs(self):
        sql = "select * from orders"
        return sql

    def get_logs_by_product(self, product):
        sql = "select * from orders where product = {}".format(product)
        return sql


'''save = input("Do you wish to save the record (Yes/ No)? ")

        save.lower()
        if save == "yes":
            self.orders_logger.write(sql)

    def update_log(self, customerid, orderid, product, units_sold, revenue, cost):
        self.customerid = customerid
        self.orderid = orderid
        self.product = product
        self.units_sold = units_sold
        self.revenue = revenue
        self.cost = cost
        self.date = str(datetime.datetime.today().date())

        sql = ("update into orders values('{customerid}','{orderid}','{product}',{units_sold},'{date}',{revenue},"
               "{cost})").format(
            vars(self))
        print(sql)

        update = input("Do you wish to update the record (yes/no)")
        if update.lower() == "yes":
            self.orders_logger.write(sql)

    def delete_log(self):
        self.customerid = int(input("Enter the log id: "))

        sql = "delete from orders where customerid = {customerid}".format_map(vars(self))

        print(sql)

        delete = input("Do you wish to delete the Record (yes/no)")
        if delete.lower() == "yes":
            self.orders_logger.write(sql)

    def get_all_logs(self):
        sql = "select * from orders"
        self.orders_logger.write(sql)

    def get_logs_by_product(self, product):
        sql = "select * from orders where product = {}".format(product)
        self.orders_logger.read(sql)


print("______________________\n\n    WELCOME    \n\n ORDERS LOGGER APP \n\n ______________________")

while True:
    print("1. Insert a new order log :")
    print("2. Update an existing order log :")
    print("3. Delete an existing order log :")
    print("4. Fetch all order logs :")
    print("5. Fetch all order logs by Product :")

    option = int(input("Enter your desired Option : "))

    if option == 1:
        print("Create a new order log")
        logger = orderlogger()
        logger.save_log()

    elif option == 2:
        print("Update an existing order log")
        logger = orderlogger()
        logger.update_log()

    elif option == 3:
        print("Delete an existing order log")
        logger = orderlogger()
        logger.delete_log()

    elif option == 4:
        print("Fetch all order logs")
        logger = orderlogger()
        logger.get_all_logs()

    elif option == 5:
        print("Fetch all orders by Product ")
        logger = orderlogger()
        logger.get_logs_by_product(input("Enter Product :"))

    else:
        print("Invalid Option")

    choice = input(" Would you like to add another order log .. ?(yes/no)")
    if choice.lower() == "no":
        break
'''
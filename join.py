from CLASS_MYSQL import  Mysql

user3 = Mysql("localhost","miki","mikirif04877",3306,"northwind")
print(user3.execute('select  Orders.ID, Customers.first_name,customers.last_name FROM Orders INNER JOIN Customers ON Orders.Customer_ID=Customers.ID',"select"))



from CLASS_MYSQL import Mysql

user1 = Mysql("localhost","root","mikirif04877","3306","sakila")

user1.connect()
print(user1.execute('select * from actor','select'))
print(user1.execute('select * from film ',"select"))
print(user1.execute('select count(*) from actor',"select"))
print(user1.execute('select count(*) from film ',"select"))
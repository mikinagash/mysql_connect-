from CLASS_MYSQL import Mysql

user2 = Mysql("localhost","miki","mikirif04877",3306,"miki_nagash")
user2.execute("update students set age = 25 where first_name ='miki'",'')
user2.execute("update students set age = 25 where first_name ='fasil'","")
user2.execute("update students set age = 32  where first_name = 'eli'","")
user2.execute("update students set city = 'adis' where first_name = 'eli'","")
user2.execute("update students set age = 29 where first_name = 'daniel'","")
user2.execute()


print(user2.execute('select * from students','select'))

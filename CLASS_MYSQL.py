import mysql.connector
class Mysql:
    def __init__(self,host,user,password,port,database):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database

    def connect(self):
        database = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database
        )
        return database

    def execute(self,query,q_type):
        db = self.connect()
        mycursor = db.cursor()
        mycursor.execute(query)
        if q_type == 'select':
            table_name = mycursor.fetchall()
            x = []
            for i in table_name:
                x.append(i)
            return "\n".join(map(str,x))

        else:
           db.commit()









# mycursor.execute('select * from students')
# students = mycursor.fetchall()
#
# for i in students:
#
#     print("student name :" + i[1])
#     print( 'student age :' ,i[5])




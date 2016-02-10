import sqlite3
import pudb


class Model:
    def __init__(self):
        self.id = id
        #self.filename = 
        #self.name = name
        #self.class_name = class_name
        #self.table_name = table_name
        

    @classmethod
    def all(cls):
        conn  = sqlite3.connect("babyorm.db")

        table_name = cls.__name__

        print(table_name)

        # get table name

        # 2 get 

        cursor = conn.cursor()
        cursor.execute(

           

            """ SELECT * FROM {}""".format(table_name,)
            )

#""" SELECT * FROM %s"""%(table_name))
# """ SELECT * FROM {}""".format(table_name))

        row =cursor.fetchall()
        conn.commit()
        conn.close()
        print(row)

        return row 


    @classmethod
    def get(cls, **kwargs):
        conn  = sqlite3.connect("babyorm.db")
        cursor = conn.cursor()
        table_name = cls.__name__

        for key, value in kwargs.items():
            columkey = key
            columvalue = value 


        cursor.execute(

            """ SELECT * FROM {} Where {} = \"{}\";""".format(table_name, columkey, columvalue))
        row =cursor.fetchone()
        conn.commit()
        conn.close()

        print(row)
        

    @classmethod
    def filter(cls, **kwargs):
        conn  = sqlite3.connect("babyorm.db")
        cursor = conn.cursor()
        table_name = cls.__name__

        for key, value in kwargs.items():
            columkey = key
            columvalue = value 

 
        c = """ SELECT * FROM {} Where {} = \"{}\" ;""".format(table_name, columkey, columvalue)
        cursor.execute(c)
        print(c)
        row =cursor.fetchall()
        conn.commit()
        conn.close()

        print(row)
        


# don't touch the code for these
class Users(Model):
    pass


class Stocks(Model):
    pass

Users.all()
#Stocks.all()
dic={"name":"Myles","name":"Sandra"}
Users.get(**dic)
Users.filter(**dic)
#Stocks.all()
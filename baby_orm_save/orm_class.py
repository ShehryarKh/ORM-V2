import sqlite3
import pudb


class Model:
    def __init__(self, **kwargs):
        self.id = id
        for key, value in kwargs.items():
            setattr(self, key, value)
        

    @classmethod
    def all(cls):
        conn  = sqlite3.connect("babyorm.db")

        table_name = cls.__name__

        print(table_name)

        cursor = conn.cursor()
        cursor.execute(

            """ SELECT * FROM {}""".format(table_name,)
            )

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
        

    @classmethod
    def save(cls, **kwargs):
    	conn = sqlite3.connect("babyorm.db")
    	cursor = conn.cursor()
    	table_name = cls.__name__

    	for key, value in kwargs.items():
            columkey = key
            columvalue = value

    	cursor.execute(
    		""" INSERT INTO {};""".format(table_name)
    		)





# don't touch the code for these
class Users(Model):
    pass


class Stocks(Model):
    pass

print(Users.all())
dic={"name":"Myles","name":"Sandra"}
#Users.get(**dic)
#Users.filter(**dic)
#Stocks.all()
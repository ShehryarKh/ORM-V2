import sqlite3

conn = sqlite3.connect('babyorm.db')
c = conn.cursor()

class Model:
	def __init__(self, **kwargs):
		for i in kwargs.keys():
			setattr(self, i, kwargs[i])

	@classmethod
	def all(cls):
		query = "SELECT * FROM {}".format(cls.__name__)
		c.execute(query)
		conn.commit()
		object_list = []
		for i in c.fetchall():
			blargs = {str(c.description[j][0]):i[j] for j in range(len(i))}
			object_list.append(cls(**blargs))
		return object_list

	@classmethod
	def get(cls, **kwargs):
		x = ["{}='{}'".format(i,kwargs[i]) for i in kwargs.keys()]
		y = ' AND '.join(x)
		query = """SELECT * FROM {} WHERE {} LIMIT 1;""".format(cls.__name__, y)
		c.execute(query)
		conn.commit()
		data = c.fetchone()
		return cls(**{str(c.description[j][0]):data[j] for j in range(len(data))})

	@classmethod
	def filter(cls, **kwargs):
		x = ["{}='{}'".format(i,kwargs[i]) for i in kwargs.keys()]
		y = ' AND '.join(x)
		query = """SELECT * FROM {} WHERE {};""".format(cls.__name__, y)
		c.execute(query)
		conn.commit()
		object_list = []
		for i in c.fetchall():
			blargs = {str(c.description[j][0]):i[j] for j in range(len(i))}
			object_list.append(cls(**blargs))
		return object_list

	def save(self):
		if hasattr(self, 'id'):
			vtu = self.update_string_helper(**self.__dict__)
			query = """UPDATE {} SET {} WHERE id={}""".format(self.__class__.__name__, vtu, self.id)
			c.execute(query)
			conn.commit()
		else:
			kwargs = self.create(**self.__dict__).__dict__
			for key, value in kwargs.items():
				setattr(self, key, value)

	@classmethod
	def create(cls, **kwargs):
		col_names, vals = cls.create_string_helper(**kwargs)
		query = """INSERT INTO {} ({}) VALUES ({})""".format(cls.__name__, col_names, vals)
		c.execute(query)
		conn.commit()
		return cls.get(id=c.lastrowid)

	@staticmethod
	def update_string_helper(**kwargs):
		x = ("{}='{}'".format(key, value) for key, value in kwargs.items() if key != 'id')
		update_str = ' AND '.join(x)
		return update_str

	@staticmethod
	def create_string_helper(**kwargs):
		cols, vals = list(zip(*kwargs.items()))
		return ','.join(cols), ','.join("'{}'".format(i) for i in vals)

### Don't touch the code for these.
class Users(Model):
	pass

class Stocks(Model):
	pass

if __name__ == '__main__':
	timmy = Users(name='Timmy', id=45, house='tree')
	print(timmy.id, timmy.house)

	print("Stocks.all()")
	for i in Stocks.all():
		print(i.id, i.symbol, i.price)

	print("Users.get(name='Harlan')")
	x = Users.get(name='Harlan')
	print(x.id, x.name, x.address, x.balance)

	print("Users.filter(name='Dr.', id=1)")
	for i in Users.filter(name='Dr.', id=1):
		print(i.id, i.name, i.address, i.balance)

	conn.close()

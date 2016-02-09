import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()

class Model:
	def __init__(self, **kwargs):
		self.columns = self.__columns()
		for key, value in kwargs.items():
			if key in self.columns:
				setattr(self, key, value)

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
			query = """UPDATE {} SET {} WHERE id=?""".format(self.__class__.__name__, vtu)
			c.execute(query, (self.id,))
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

	def delete(self, id_):
		c.execute("""DELETE FROM {} WHERE id={}""".format(self.__class__.__name__, id_))
		conn.commit()
		return None

	def update_string_helper(self, **kwargs):
		x = ("{}='{}'".format(key, value) for key, value in kwargs.items() if key != 'id' and key in self.columns)
		update_str = ', '.join(x)
		return update_str

	@staticmethod
	def create_string_helper(**kwargs):
		cols, vals = list(zip(*((key, value) for key, value in kwargs.items() if key != 'columns')))
		return ','.join(cols), ','.join("'{}'".format(i) for i in vals)

	def __columns(self):
		c.execute("""PRAGMA table_info('{}')""".format(self.__class__.__name__))
		return [i[1] for i in c.fetchall()]

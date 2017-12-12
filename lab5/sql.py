import sqlite3

class Sqlite:
	def __init__(self, dbName):
		self.dbName = dbName
		self.Connection = sqlite3.connect(dbName)
		self.Cursor = self.Connection.cursor()

	def close(self):
		self.Connection.close()
	def createTable(self, tableName, rows):
		values = ''
		for name, value in rows.items():
			values += name + ' ' + value + ', '
		values = values[0:-2]
		self.Cursor.execute("DROP TABLE IF EXISTS " + str(tableName))
		self.Cursor.execute('''CREATE TABLE ''' + str(tableName) + '''(''' + values + ''')''')
		self.commit()

	def insertIntoTable(self, tableName, data=None):
		parametrs = '?,' * data[0].__len__()
		parametrs = parametrs[0:-1]
		self.Cursor.executemany('INSERT INTO ' + tableName +' VALUES ' + '(' +parametrs + ')', data)
		self.commit()

	def select(self, query):
		self.Cursor.execute(query)




	def commit(self):
		self.Connection.commit()
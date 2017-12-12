from sql import *

tableName = 'Book'
countOfUnique = 'SELECT COUNT(DISTINCT second_name_author) FROM ' + tableName 
oldest = 'SELECT name FROM ' + tableName + ' ORDER BY year_of_publication ASC LIMIT 1 '

entrantTable = {'id': 'integer', 'first_name_author': 'str', 'second_name_author': 'str', 'name': 'str', 'number_of_page': 'str', 'year_of_publication': 'int', 'name_of_publishing_house':'str', 'date_of_arrival':'str'}
data = [('1', 'Roma', 'chubk', 'Math', 5, 1900, 'BLA', '11/12/2000'),
        ('2', 'Roma', 'NEchubk', 'NEMath', 5, 1901, 'BLA', '11/12/2000')]

DB = Sqlite('DB.sqlite31')
DB.createTable(tableName, entrantTable)
DB.insertIntoTable('Book', data)

DB.select(countOfUnique)
print(DB.Cursor.fetchone()[0])

DB.select(oldest)
print(DB.Cursor.fetchone()[0])

DB.close()
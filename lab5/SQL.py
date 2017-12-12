import sqlite3 as lite
class SQL:
    def __init__(self, name):
        self.con = lite.connect(name)

    def __del__(self):
        self.con.close()

    def init_DB(self):
        self.con.execute("DROP TABLE IF EXISTS Book;")
        self.con.execute('''CREATE TABLE Book
                   (id INTEGER PRIMARY KEY AUTOINCREMENT    NOT NULL,
					first_name_author CHAR(50)NOT NULL,
					second_name_author CHAR(50)NOT NULL,
					name CHAR(50) NOT NULL,
					number_of_page INT,
					year_of_publication INT NOT NULL,
					name_of_publishing_house CHAR(50),
					date_of_arrival DATE);''')
        self.con.commit()

    def add(self, book):
        self.con.execute("INSERT INTO Book (first_name_author, second_name_author, name, number_of_page, year_of_publication, name_of_publishing_house, date_of_arrival) VALUES (?, ?, ?, ?, ?, ?, ? )",
                                            book.first_name_author, book.second_name_author,book.name,book.number_of_page,book.year_of_publication,book.name_of_publishing_house,book.date_of_arrival);
        self.con.commit()

    def count_unique_authors(self):
        cursor =  self.con.execute("SELECT COUNT(DISTINCT second_name_author) FROM Book;")
        return cursor.fetchone()[0]

    def print(self):
        cursor = self.con.execute("SELECT * FROM Book;")
        
        print(cursor.fetchall())

    def find_oldest_book(self):
        cursor = self.con.execute("SELECT name FROM Book ORDER BY year_of_publication DESC LIMIT 1;")
        return cursor.fetchone()


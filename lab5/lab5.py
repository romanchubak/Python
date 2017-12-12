import ZODB
import ZODB.FileStorage
from SQL import SQL
from datetime import date
import transaction

class Book(object):
    def __init__(self, first_name_author = "first_name_author", second_name_author = "second_name",name = "book", number_of_page = 0, year_of_publication = 1900,name_of_publishing_house = "vydavnyctvo", date_of_arrival = date.today()):
        self.first_name_author = first_name_author
        self.second_name_author = second_name_author
        self.name = name
        self.number_of_page = number_of_page
        self.year_of_publication = year_of_publication
        self.name_of_publishing_house = name_of_publishing_house
        self.date_of_arrival = date_of_arrival


def find_oldest_book(arr):
    oldest = Book(year_of_publication=2018)
    for a in arr:
        if oldest.year_of_publication > a.year_of_publication:
            oldest = a
    return oldest
def find_unique_athors(arr,n):
    output = []
    for i in range(0,n):
        if arr[i] in arr:
            output.append(arr[i])
    return output.count()

n = int(input("input number of books: "))
books = []
for i in range(0,n):
   first_name_author = input("input first name of auther: ")
   second_name_author = input("input first name of auther: ")
   name = input("input first name of book: ")
   number_of_page = int(input("input number of page: "))
   year_of_publication = int(input("input year of publication: "))
   name_of_publishing_house = input("input first name of publication house: ")
   date_of_arrival = date.today()


   
#storage = ZODB.FileStorage.FileStorage("mydata.fs")
#db = ZODB.DB(storage)
#connection = db.open()
#root = connection.root

#root.items = []
#for book in books:
#    root.append(book)

#transaction.commit()
#print("oldest book in zodb : ")
#print(find_oldest_book(root.items).name)
#print("count of unique")


sql = SQL("test.sqlite")
sql.init_DB()
for book in books:
    sql.add(book)
print(sql.print())
print("oldest book in sql : ")
print(sql.find_oldest_book())
print("count of unique authors : ")
print(sql.count_unique_authors())


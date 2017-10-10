
from datetime import date
class Person(object):
    def __init__(self, first_name = "first_name", second_name = "second_name", birthday = date.today()):
        self.FirstName = first_name
        self.SecondName = second_name
        self.Birthday = birthday
    def GetYears(self):
        return date.today().year - self.Birthday.year  
    def Input(self):
        self.FirstName = input("input First name: ")
        self.SecondName = input("input Second name: ")
        year = input("input year: ")
        month = input("input month: ")
        day = input("input day: ")
        self.Birthday = date(int(year),int(month),int(day))
    def __str__(self):
        return "First name: " + self.FirstName +"\nSecond name: " + self.SecondName + "\nBirthday: " + str(self.Birthday)
        



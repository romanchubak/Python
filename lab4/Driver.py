from datetime import date
from Person import Person
class Driver(Person):
    def __init__(self, first_name = "first_name", second_name = "second_name", birthday = date.today(), distance = 0, price = 0, lable = "zaz"):
        Person.__init__(self, first_name, second_name, birthday)
        self.Distance = distance
        self.PricePerKm = price
        self.LableOfCar = lable
    def Input(self):
        Person.Input(self)
        self.Distance = int(input("input distance: "))
        self.PricePerKm = int(input("input price per km: "))
        self.LableOfCar = input("input labal of car: ")
    def GetSalary(self):
        return "salary of "+ self.FirstName + " is " + str(self.Distance*self.PricePerKm)
    def __str__(self):
        return Person.__str__(self) + "\nDistance: " + str(self.Distance) + "\nPrice Per Km: " + str(self.PricePerKm) + "\nLabel of car: " + str(self.LableOfCar) 
    def __lt__(self,b):
        return  self.GetYears() < b.GetYears()
    def __gt__(self,b):
        return  self.GetYears() > b.GetYears()



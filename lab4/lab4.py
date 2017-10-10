from datetime import date
from Person import Person
from Driver import Driver
def main():
    n = int(input("input n: "))
    drivers = []
    for i in range(0,n):
        x = Driver()
        x.Input()
        drivers.append(x)
    drivers.sort()
    for i in range(0,n):
        print(drivers[i].GetSalary())
    print("the older is : " + str(drivers[0]))
main()
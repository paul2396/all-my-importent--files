class Employee:
   empCount=0
     def __init__(self, first, last, address, email, pay):
        self.first = first
        self.last = last
        self.address = address
        self.email = email
        self.pay = pay

     def fullname(self):
        return "{} {}".format(self.first, self.last)

employee1 = Employee("Paul", "Jones", "32 Ley court Millbank london Xw21", "ted@hotmail.com", "2300")
employee2 = Employee("Bill", "Smith", "230 Waybank road ManchesterLA3RG", "bill@hotmail.com", "3200")


print(employee1.__dict__)
print(employee1.fullname())






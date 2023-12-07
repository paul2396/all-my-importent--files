
# Define the Planet class
class Planet:
    # Constructor (initializer)
    def __init__(self, name, distance_from_sun, radius):
        self.name = name
        self.distance_from_sun = distance_from_sun  # in million kilometers
        self.radius = radius  # in kilometers

    # Method to get the surface area of the planet
    def surface_area(self):
        return 4 * 3.14159265359 * self.radius**2  # Assuming pi is approximately 3.14159265359

    # Method to get the volume of the planet
    def volume(self):
        return (4/3) * 3.14159265359 * self.radius**3

# Create instances of the Planet class
planet1 = Planet("Mars", 225.0, 3389.5)
planet2 = Planet("Saturn", 1426.7, 58232.0)

# Access attributes and methods of the Planet instances
print(f"{planet1.name}:")
print(f"Distance from Sun: {planet1.distance_from_sun} million kilometers")
print(f"Surface Area: {planet1.surface_area()} square kilometers")
print(f"Volume: {planet1.volume()} cubic kilometers")

print("\n")

print(f"{planet2.name}:")
print(f"Distance from Sun: {planet2.distance_from_sun} million kilometers")
print(f"Surface Area: {planet2.surface_area()} square kilometers")
print(f"Volume: {planet2.volume()} cubic kilometers")

#!=================================================================

 class TopTenCheapestCars:
    def __init__(self, make: str, engine: str, mpg: str, seats: int, cost: float):
        self.make = make
        self.engine = engine
        self.mpg = mpg
        self.seats = seats
        self.cost = cost

    def formatted_cost(self):
        # Format the cost with pound symbols and commas for thousands
        return f'£{self.cost:,.2f}'

# Now you can create instances of the TopTenCheapestCars class
car1 = TopTenCheapestCars("Kia Picanto", "58HP", "mpg 48.7", 5, 13665.00)
# ...
# Create more instances as needed


car1 = TopTenCheapestCars("Kia Picanto", "58HP","mpg 48.7", 5, 13665.00)
car2 = TopTenCheapestCars("Suzuki Swift", "59HP","mpg 57.2", 5, 16849.00)
car3 = TopTenCheapestCars("Toyota Aygo", "58HP","mpg 58.5", 4, 14638.00)
car4 = TopTenCheapestCars("Volkswagen Up", "55HP","48.7", 4, 15155.00)
car5 = TopTenCheapestCars("Mazda", "60HP","mpg 57.9", 5, 17375.00)
car6 = TopTenCheapestCars("Suzuki Ignis","65HP","mpg 54.4",4, 1399.00)
car7 = TopTenCheapestCars("Renault Clio","75HP","mpg 47.9", 5,15895.00)
car8 = TopTenCheapestCars("Hyundai I20","99HP","mpg 47.1", 5, 15195.00)
car9 = TopTenCheapestCars("Kia Rio","83HP","mpg 50.4", 5, 14045.00)
car10 = TopTenCheapestCars("Dacia Sandero","89HP","mpg 48.7",5, 8995.00)
car11 = TopTenCheapestCars("Hyundai I10","99HP","mpg 47.1",5, 15195.00)
car12 = TopTenCheapestCars("MG3","105HP","mpg 47.1", 5, 9995.00)


#!Find the cheapest car
cheapest_car = car1  #!Initialize with the first car
for car in [car2, car3, car4, car5, car6, car7, car8, car9, car10, car11, car12]:
    if car.cost < cheapest_car.cost:
        cheapest_car = car #!Initialize with the first car

#!Find the most expensive car
most_expensive_car = car1 
for car in [car2, car3, car4, car5, car6, car7, car8, car9, car10, car11, car12]:
    if car.cost > most_expensive_car.cost:
        most_expensive_car = car

# Print the results
print(f"The cheapest car is {cheapest_car.make} with a cost of {cheapest_car.formatted_cost()}.")
print(f"The most expensive car is {most_expensive_car.make} with a cost of {most_expensive_car.formatted_cost()}.")


#!===============================================
import logging
class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, annual_salary, dob, address, length_of_service, job_title):
        self.name = name
        self.annual_salary = annual_salary
        self.dob = dob
        self.address = address
        self.length_of_service = int(length_of_service.split()[0])  # Store as an integer
        self.job_title = job_title
        Employee.empCount += 1

    def __str__(self):
        return (
            f"Name: {self.name},\n"
            f"Annual Salary: {self.annual_salary},\n"
            f"DOB: {self.dob},\n"
            f"Address: {self.address},\n"
            f"Length of Service: {self.length_of_service} years,\n"
            f"Job Title: {self.job_title}"
        )
employees = []

employee1 = Employee(

    "Joe Blogs",
    27000,
    "17/08/1979",
    "25 hill road Boston USA",
    "14 years",
    "fitter"
)
employees.append(employee1)
        
employee2 = Employee(
    "Jean Simms", 
    2400, 
    "23/09/1990", 
    "14 sumerset road Boston USA", 
    "5 years", 
    "secretary"
    )
employees.append(employee2)

employee3 = Employee(
    "Billy Janes", 
    2600, 
    "14/10/1980", 
    "827 Puzim Lane Boston USA", 
    "6 years", 
    "production"
    )
employees.append(employee3)

employee4 = Employee(
    "Ted Proctor", 
    2700, 
    "10/08/1972", 
    "1504 Nicuk View Boston USA", 
    "19 years", 
    "shift supervisor"
    )
employees.append(employee4)

employee5 = Employee(
    "Suzan Page", 
    2600, 
    "03/09/2006",
    "290 Sulev Boulevard Boston USA", 
    "5 years", 
    "production"
    )
employees.append(employee5)

employee6 = Employee(
    "Jenny Gillingham",
    2600, 
    "21/07/2004",
    "266 Zakwaw Plaza Boston USA", 
    "7 years", 
    "production"
    )
employees.append(employee6)

employee7 = Employee(
    "Ann Brent", 
    2600, 
    "21/07/2007", 
    "1644 Tawpuc Center Boston USA", 
    "5 years", 
    "production")
employees.append(employee7)


print(employee3)
#!===================================================================












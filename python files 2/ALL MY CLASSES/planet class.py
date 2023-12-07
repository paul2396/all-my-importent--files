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
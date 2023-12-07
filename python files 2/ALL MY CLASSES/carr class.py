# Create car objects
car1 = TopTenCheapestCars("Kia Picanto", "58HP", "48.7 mpg", 5, 13665.00)
car2 = TopTenCheapestCars("Suzuki Swift", "59HP", "57.2 mpg", 5, 16849.00)

# Calculate and print the price difference
price_diff = car1.price_difference(car2)
print(f"The price difference between Car 1 and Car 2 is £{price_diff:,.2f}")

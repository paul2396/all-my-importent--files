

#! my learning curve
#!first i will deal with lists?

from turtle import title


my_list=[20,89,34,76,12,900,34,65,56,34,700,300,7,400,79,90,89,10]
print(my_list)
print(my_list[0])#!when you use this function it prints the first item in a list
print(my_list[-1])#! using the function will print the last item in a list
my_list[2] = 90 #!This line modifies the element at index 2 (which is the third element in the list) and changes it to 90.
print(my_list)
 #!=======================================================================
 #!next is the range function
 #!The range() function returns a sequence of numbers between the given range.
for i in range(0, 10):
    print(i)
# Example 2: Range with start=2, end=10, step=2
for i in range(2, 10, 2):
    print(i)
# Output: 2 4 6 8
#! the code above gives you from 2 upto 10 in steps of 2
#however i can chang it to a lot of different codes
for i in range(10,100,5):
    print(i)
#!===========================================
#!Example: Using for, if, and else with the range function
#!Iterating through a range of numbers
for i in range(1, 11):
    #!Checking if the number is even
    if i % 2 == 0:
        print(f"{i} is an even number.")
    else:
        print(f"{i} is an odd number.")
#!Checking for a specific condition
    if i == 5:
        print(f"{i} is equal to 5.")
    elif i > 5:
        print(f"{i} is greater than 5.")
    else:
        print(f"{i} is less than 5.")
#!========================================================
#!if-else block" or "if-else statement."

x=100
y=100
if x<y:
    print("x is not equal to y")
else:
    print("x is equal to y")
#!================================  
x=5
y=10
if x > y:
  print("x is greater than y")

elif x < y:
  print("x is less than y") 
else:
  print("x is equal to y")

a=800
b=300
if a>b:
    print("b is greater than a")
else:
    print("you must be joking")
#!========================================================
# Assuming you have some way of obtaining the age, such as user input or a predefined value
age = 105  # You can replace this with the actual age you want to check

if age > 120:
    print("How are you even alive?")
elif age > 100:
    print("You're old")
else:
    print("You may have some years left in you")
#!==================================================
if age > 50:
    print("you are not that old")
elif age <= 50 and age > 45:
    print("you are not old")
else:
    print("You may have some years left in you")
#!======================================================
class Book:
    def __init__(self, title, author, genre, publication_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Genre: {self.genre}\n"
            f"Publication Year: {self.publication_year}"
        )

class FictionBook(Book):
    def __init__(self, title, author, genre, publication_year, protagonist):
        super().__init__(title, author, genre, publication_year)
        self.protagonist = protagonist

    def __str__(self):
        return super().__str__() + f"\nProtagonist: {self.protagonist}"


fiction_book1 = FictionBook(
    title="The Great Gatsby",
    author="F. Scott Fitzgerald",
    genre="Fiction",
    publication_year=1925,
    protagonist="Jay Gatsby"
)
fiction_book2 = FictionBook(
    title="The Last Crossing", 
    author="Guy Vanderhaeghe",  
    genre="fiction",
    publication_year=2004,  
    protagonist="Charles and Addington Gaunt"
)
fiction_book3 = FictionBook(
    title="Wolf Hall",  
    author="Hilary Mantel",  
    publication_year=2010,  
    protagonist="Thomas Cromwell"
)


non_fiction_book1 = Book(
    title="Social history of the English countryside",
    author="G.E. Mingay",
    genre="Non-fiction",
    publication_year=1990
)

non_fiction_book2 = Book(
    title="The Death of Rural England",
    author="Allan Howkins",
    genre="Non-fiction",
    publication_year=2003
)

non_fiction_book3 = Book(
    title="Work Gender and Family in Victorian England",
    author="Karl Ittmann",
    genre="Non-fiction",
    publication_year=1995
)

non_fiction_book4 = Book(
    title="The Cambridge Economic History of Modern Britain 1700_1860",  # Removed extra quotes
    author="Roderick Floud",
    genre="Non-fiction",
    publication_year=2004
)

                      
# Print the details of the books
print(fiction_book1)
print("\n")
print(fiction_book2)
print("\n")
print(fiction_book3)
print("\n")
print(non_fiction_book1)
print("\n")
print(non_fiction_book2)
print("\n")
print(non_fiction_book3)
print("\n")
print(non_fiction_book4)




            







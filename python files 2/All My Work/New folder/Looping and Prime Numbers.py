for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
#!========================================
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
#!========================================
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
#!===========================================
!==========================================================
print("Python is awesome".capitalize())  # Output: "Python is awesome"

print("PYTHON IS KING".lower())  # Output: "python is king"

print("python is hot".upper())  # Output: "PYTHON IS HOT"

print("Harry potter and the half-blood prince".title())  # Output: "Harry Potter And The Half-Blood Prince"

print("AVENGER:the war of infinity".swapcase())  # Output: "avenger:THE WAR OF INFINITY"
#!======================================================================

#!In this example, we illustrate how words can be sorted lexicographically (alphabetic order).
#!the code below will give you all the word in the test but in alphabetically
#!alphabeticallyery goos must keep!!
y_str = "The quick brown fox jumps over the lazy dog"

# Breakdown the string into a list of words
words = [word.lower() for word in y_str.split()]

# Sort the list
words.sort()

# Display the sorted words
print("The sorted words are:")
for word in words:
    print(word)
#!====================================================
l1 = [10,20,30,40,50]


d1 = {101:"Ravi",102:"Mohan",103:"Kumar"}
print(d1[101])
print(d1[102])
print(d1[103])


#!=====================================================

t = (10,20.25,"sathya",False)
print(t) #!This line prints the entire tuple t. The output will be:
print(t[1])#!This line prints the element at index 1 of the tuple, which is 20.25. The output will be:
print(t[-1]) #!This line prints the last element in the tuple, which is at index -1. The output will be:

print("----------------------")
t1 = (10,20,30,40,50,20,40,50,20,20,20)
no = t1.count(20)#!These lines count how many times the 
#!#value 20 appears in the tuple t1 and prints the count. 
print(no)


print("----------------------")
t1 = (10,20,30,40,50,20,40,50,20)
pos = t1.index(20) #!These lines find the index of the first occurrence of the value 20
print(pos)
#!==========================================================
print("---------------------------")
d1 = {"idno":101,"name":"Ravi","salary":125000.00}
print(d1)
d1["status"] = True
print(d1)
d1.setdefault("designation")
print(d1)
val = d1.setdefault("status")
print(val)
#!====================================================

#!The code below demonstrates various string manipulation operations in Python,
s1 = "billy"
new_s = s1.upper()
print(new_s)

s2 = "PYTHON"
new_s = s2.lower()
print(new_s)
s3 = "My name is Ted so do not forget" #!This line defines a string s3 
#!with a mix of uppercase and lowercase letters.
new_s = s3.swapcase()
print(new_s)

s4 = "hello this is Paul from Sidney"
new_s = s4.title()
print(new_s) #!This line prints the length of the 
#!string new_s after removing the trailing whitespace.

s5 = "hello this is naveen from sathya"
new_s = s5.capitalize()
print(new_s)
#!============================================================

#!below using the function to get items from a list
s1 = "python"
print(s1[0]) # p
print(s1[-1]) # n
print(s1[3])
#!=========================================
s3=("what is the point of all this")
print(s3[10])
#!========================================




a = 5
b = 9

a, b = b, a

print(a, b)
#!=====================================================================


#!=======================================================
#! using better comments the #! will give you red
#? will give you blue
#todo this is anothr comment
#?===============================================================
#!The code below defines a class p with a constructor (__init__) that sets an attribute x, 
#!# and a method display_p that prints the value of x.
#!t then creates an instance of the class, sets x to 42, and prints the value using display_p.
class p:
  def __init__(self, x):
    self.x = x
  def display_p(self):
    print(self.x)

# Define the class
class p:
    def __init__(self, x):
        self.x = x
    
    def display_p(self):
        print(self.x)

# Create an instance of the class
my_instance = p(42)

# Call the display_p method to print the value of 'x'
my_instance.display_p()
#!=========================================================
#! The code below defines a Python class named 
class p:
  def __init__(self, x):
    self.x = x
  def display_p(self):
    print(self.x)    
#!==========================================================
#!Example: add two matrices using nested loop
X = [[12,9,3],
    [4,5,6],
    [7,8,3]]

Y = [[9,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

#!iterate through rows
for i in range(len(X)):
   ##!iterate through columns
   for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)
#!================================================
#!In this example, we illustrate how words can be sorted lexicographically (alphabetic order).
#!the code below will give you all the word in the test but in alphabetically
#!alphabeticallyery goos must keep!!
y_str = "The quick brown fox jumps over the lazy dog"

# Breakdown the string into a list of words
words = [word.lower() for word in y_str.split()]

# Sort the list
words.sort()

# Display the sorted words
print("The sorted words are:")
for word in words:
    print(word)
#!====================================================

t = (10,20.25,"sathya",False)
print(t) #!This line prints the entire tuple t. The output will be:
print(t[1])#!This line prints the element at index 1 of the tuple, which is 20.25. The output will be:
print(t[-1]) #!This line prints the last element in the tuple, which is at index -1. The output will be:

print("----------------------")
t1 = (10,20,30,40,50,20,40,50,20,20,20)
no = t1.count(20)#!These lines count how many times the 
#!#value 20 appears in the tuple t1 and prints the count. 
print(no)


print("----------------------")
t1 = (10,20,30,40,50,20,40,50,20)
pos = t1.index(20) #!These lines find the index of the first occurrence of the value 20
print(pos)
#!==========================================================
print("---------------------------")
d1 = {"idno":101,"name":"Ravi","salary":125000.00}
print(d1)
d1["status"] = True
print(d1)
d1.setdefault("designation")
print(d1)
val = d1.setdefault("status")
print(val)
#!====================================================

#!The code below demonstrates various string manipulation operations in Python,
s1 = "sathya"
new_s = s1.upper()
print(new_s)

s2 = "PYTHON"
new_s = s2.lower()
print(new_s)
s3 = "Naveen Kumar From SathyaTech" #!This line defines a string s3 
#!with a mix of uppercase and lowercase letters.
new_s = s3.swapcase()
print(new_s)

s4 = "hello this is naveen from sathya"
new_s = s4.title()
print(new_s) #!This line prints the length of the 
#!string new_s after removing the trailing whitespace.

s5 = "hello this is naveen from sathya"
new_s = s5.capitalize()
print(new_s)
#!============================================================

s6 = "   Python"
print(len(s6))
new_s = s6.lstrip()
print(len(new_s))

s7 = "Python          "
print(len(s7))
new_s = s7.rstrip()
print(len(new_s))

s8 = "     Python          "
print(len(s8))
new_s = s8.strip()
print(len(new_s))
s1 = "sathya"
new_s = s1.upper()
print(new_s)
#! some good code above
#!====================================
#!below using the function to get items from a list
s1 = "python"
print(s1[0]) # p
print(s1[-1]) # n
print(s1[3])
#!=========================================
s3=("what is the point of all this")
print(s3[10])
#!========================================


def func(x, y):
    return x+y
print(type(func))

show = print
show("something")

name = ["jatin", "gt", "afreed", "shiva", "guru"]
for item in enumerate(name):
    print(item)

a = 5
b = 9

a, b = b, a

print(a, b)
#!=====================================================================
#!Below is a great bit of code nonot delete it
from turtle import *

# Welcome this is the turtle tutorial
# Turtle library is a drawing library check them out on
# https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.speed

# To make a square we have to move forward then a direction 4 times.

for i in range(4): # Start a loop
    forward(100) # Move forward
    right(90)  # Turn

# Now we just need to make a circle by a square
# To make it easy for us let us make a function to the square

def square():
    for i in range(4):
        forward(50)
        right(60)
        speed(15)
#     return None

for i in range(360):
    square()
    right(1)
    speed(15)

# And if you want to speed up stuff and get the result faster
# speed(10) # 0 is the fastest while 1 is the slowest, 10 is fast

# Have fun and try out different challenges
#!==============================================================
def hexagon():
    for i in range(6):
        forward(50)
        right(60)

for i in range(360):
    hexagon()
    right(1)
    speed(15)
#!=================================================
def square_with_color():
    begin_fill()
    pencolor("blue")  # Set pen color
    for i in range(4):
        forward(50)
        right(90)
    end_fill()
    pencolor("black")  # Reset pen color to black

for i in range(360):
    square_with_color()
    right(1)
    speed(15)
    #!==================================================
def nested_squares():
    for i in range(4):
        square_with_color()
        forward(20)
        right(90)

for i in range(90):
    nested_squares()
    right(4)
    speed(15)
#!=====================================================

    
def school_day(day):
        if day.weekday==5 or day.weekday==6:
            return False
        else:
            return True

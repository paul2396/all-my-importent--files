X = [[12, 9, 3],
     [4, 5, 6],
     [7, 8, 3]]

Y = [[9, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)
#!============================================================
my_list = [21, 33, 66, 77, 90, 67, 45, 23, 2]
for index, val in enumerate(my_list):
    print(index, val)
    my_list.sort()
#!===========================================
freq = ["a", 1, "a", 9, "a", 6, 3, 1, "a"].count("a")
print(freq)
#!============================================
# Snippet 6
my_list = [21, 33, 66, 77, 90, 67, 45, 23, 2]
for index, val in enumerate(my_list):
    print(index, val)
    my_list.sort()

# Python Program to Count the Occurrence of an Item in a List
freq = ["a", 1, "a", 9, "a", 6, 3, 1, "a"].count("a")
print(freq)
#!=============================================================
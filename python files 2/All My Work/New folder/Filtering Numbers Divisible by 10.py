my_list = [17, 34, 51, 40, 68, 70, 119, 327, 243, 900, 400, 700, 56]
result = list(filter(lambda x: (x % 10 == 0), my_list))
print("Numbers divisible by 10 are", result)
#!===================================================
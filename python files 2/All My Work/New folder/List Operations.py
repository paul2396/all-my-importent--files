my_list = [21, 33, 66, 77, 90, 67, 45, 23, 2]
for index, val in enumerate(my_list):
    print(index, val)
#!===========================================
freq = ["a", 1, "a", 9, "a", 6, 3, 1, "a"].count("a")
print(freq)
#!=========================================
data = [1, 6, 3, 4, 5, 5, 9, 4]
for x in data:
    print(x)

N = 10
for x in range(N + 1):
    print(x)
#!=======================================
#!The simplest form compares a subject value
# against one or more literals:
def http_error(status):
    match status:
        case 400:
            return"bad request"
        case 404:
            return"not found"
        case 418:
            return "i'am a tea pot"
        case _:
            return"something wrong with the internet"
status_code = 404
result = http_error(status_code)
print(result)
#!===========================================================
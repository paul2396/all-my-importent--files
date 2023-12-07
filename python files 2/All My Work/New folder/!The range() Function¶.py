!The range() Function¶
#!To iterate over the indices of a sequence,
# you can combine range() and len() as follows
w = ["neverending", "transgrees", "nevertheless"]

for i in range(len(w)):
    print(w[i])
#!=============================================
#!break and continue Statements, and else Clauses on Loops
for n in range(2,30):
    for x in range(2, n):
        if n % x ==0:
            print(n,"equals",x,"*",n//x)
            break
    else:
        print(n, "Is a prime number")

#1=================================================

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
#!=====================================================
#!The continue statement, also borrowed from C,
# continues with the next iteration of the loop:
for num in range(2,10):
    if num % 2 == 0:
          print("found an even number",num)
          continue
    print("found an odd number",num)
#!=================================================
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
#!====================================================================
#!Here is an example of a multi-line docstring:
def my_function():
    """do nothing but document i
    No realy it dosen't do anything"""
    pass
print(my_function.__doc__)
#!====================================================================

#!============================================================================ 

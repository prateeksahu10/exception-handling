# q.1 name and handle the exception
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("there is ZeroDivision error because you can not divide a number by zero")

# q.2 name and handle the exception in list
l=[1,2,3]
try:
    print(l[3])
except:
    print("there is an Index Error.")

# q.3 what will be the output of following code
print("""An exception
' after this an error occur '""")

# q.4 what will be the output of following code
print("""Output:
-5.0
a/b result in 0"""

# q.5 wrire a program of the following error
try:
    import ab
except ImportError:
    print("there is an import error because 'ab' module is not present")
try:
    c=int(input("Enter a number"))
except ValueError:
    print("Please enter a number not a string")
try:
    l=[1,2,3]
    i=int(input("Enter the index"))
    print(l[i])
except IndexError:
    print("Invalid index")

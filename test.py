#Welcome to Programming!
    #This is a comment in python!

#Values, Variables, and Data Types
    #type function 
print(type("Hello World"))
print(type(15))
print(type(True))
print(type(78.8))
print(type("78.8"))

    #type conversion
        #1. int
print(int(-3.4))
print(int(2.999))
print(int("2345"))
#print(int("23 bottles")) 
    #invalid

        #2. float
print(float(17))
print(float("123.45"))

        #3. string
print(str(17))

    #Mathematical Operation - Priority
print(84 + 10)
print(84 - 10)
print(84 * 10)
print(84 // 10)
print(84 / 10)
print(2 ** 5)
print(84 % 10)
#only when all numbers used in the operation are integers, the result is an integer.
#if any of the numbers is a float, the result is a float.
#HOWEVER, integer division with a float with yield an integer answer as a floating point rather than the correct decimal approximation. (i.e., 11//3.0 = 3.0, not 3)

    #Operations on Strings
print("Hello" + " World")
print("Hello" * 3)
print(len("Hello World"))
#n = input("Enter your name: ")
#print("Hello " + n  + "!")

    #Useful functions
print(len("Happy Birthday"))
#n = input("Enter your name: ")

#Functions
def addTwoNums (x,y) : 
    sumOfNum = x + y
    print("The sum of the two given numbers is " + sumOfNum + ".")

#Print vs Return
def tester():
    print("Hey")
    return("Bye")

x = tester()
print(x)
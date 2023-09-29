""" #ADD TWO NUMBERS
num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
sum = num1 + num2
print("Sum of two numbers {0} and {1} is {2}" .format(num1,num2,sum)) """

""" #ADDITION USING FUNCTION
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

def add(a,b):
    sum = a + b
    return sum

sum = add(num1,num2)
print("Sum of {0} and {1} is {2}".format(num1,num2,sum)) """

""" #USING LAMBDA

sum = lambda x, y: x + y

num1 = 5
num2 = 10

result = sum(num1, num2)
print("{0} + {1} = {2}".format(num1,num2,result))   """
""" 
#MAXIMUM OF TWO NUMBERS

a = int(input("Enter first number"))
b = int(input("Enter second number"))

def max(a, b):
    if a > b:
        d = "A is greater {0}" .format(a)
        return d
    else:
        d = "B is greater {0}" .format(b)
        return d
    
print(max(a,b))    """ 


""" #USING LAMBDA
max = lambda num1, num2: num1 if num1 > num2 else num2 
num1 = 10
num2 = 19

print(max(num1, num2))
 """

 #FACTORIAL OF GIVEN NUMBER
"""     
fact = lambda n: 1 if (n == 0 or n == 1) else n * fact(n-1)
n = 5

print(fact(n)) """

""" def fact(n):
    if n < 0:
        return 0
    elif (n == 0 or n == 1):
        return 1
    else:
        fact = 1
        while n > 1:
           fact *= n
           n -= 1
        return fact   

n = 5
print("Factorial is", fact(n))    """

#SIMPLE INTEREST

""" si = lambda x, y, z: (x * y * z)/100

x = 10000
y = 5
z = 5 

x = int(input("Enter x"))
y = int(input("Enter y"))
z = int(input("Enter z"))

print("Simple Interest = ", si(x,y,z)) """

""" #COMPOUND INTEREST
def compound_int(p,r,t):
    a = p * (pow(1+(r/100),t))
    ci = a - p
    print("Compound Interest", ci)

compound_int(10000, 10.25, 5)     """


#AMSTRONG NUMBER
def ams(n):
    a = n
    b = len(str(n))
    ams = 0
    while(n>0):
        r = n % 10
        ams = ams + pow(r,b)
        n = n // 10
        
   # print(ams)
    # print(a)    
    if (ams == a):
        print("Amstrong Number")
    else:
        print("Not an Amstrong number")    

n = int(input("enter number"))
ams(n)

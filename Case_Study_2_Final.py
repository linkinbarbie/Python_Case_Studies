# 1. A Robot moves in a Plane starting from the origin point (0,0). The robot can move toward UP, DOWN, LEFT, RIGHT.
# The trace of Robot movement is as given following:UP 5 DOWN 3 LEFT 3 RIGHT 2 The numbers after directions are steps.
# Write a program to compute the distance current position after sequence of movements.

import math


# Multi-dimensional point


def getDistance(a, b, aa, bb):
    print("Coordinate of Up, Down: " + str([a, b]))
    print("Coordinate of Left, Right: " + str([aa, bb]))
    ans = math.dist([a, b], [aa, bb])
    print(ans)


print(getDistance(1, 2, 3, 4))

# 2. Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list

# 2a. Set up the company's data list and sort it.
a = []  # define an empty list
companyData = ['rtr', 3, 4545, 67, 89, 'uik', 'pop', 'uy', 90, 45, 'quebec', 'alien', 'abba', 'zeo', 'ere']  # XYZ
# Company data
for x in companyData:
    a.append(str(x))  # change the elements in the company list to string

b = sorted(a)  # sorted company list
print(b)

# 2b. Write a function to allow the searching of data within the company list and return response on the results
# ake the input and search the company list for specific, variable data

d = []


def search(*datas):
    for i in b:
        for j in datas:
            if i == str(j):
                d.append(str(j))
            else:
                pass
    if len(d) == 0:
        print('The data is not in the list')
    else:
        print('The data is in the list')


search(33, 7)  # run the function to check for specific data.

# 3. Weather forecasting organization wants to show is it day or night. So, write a program for such organization to
# find whether is it dark outside or not.

import datetime


def checkdaytime():
    current_Time = datetime.datetime.now()
    print(current_Time.strftime("%H:%M"))  # show hour min time
    if 0 <= int(current_Time.strftime("%H")) < 8 or 18 <= int(current_Time.strftime("%H")) <= 23:
        print("It is dark outside")
    else:
        print("It is light outside")


checkdaytime()  # run the function

# 4. Write a program to find distance
# between two locations when their latitude and longitudes are given.

import math


def calc_Distance(e, f, g, h):
    longs = [e, f]
    lat = [g, h]
    ans = math.dist(longs, lat)
    print(ans)


calc_Distance(1, 2, 3, 4)


# 5.Design a software for bank system. There should be options like cash withdraw,
# cash credit and change password. According to user input,
# the software should provide required output.Hint:
# Use if else statements and functions.

# create a class called banking software
class banksoftware:
    def cash_withdraw(self):
        print("cash withdraw")

    def credit_card(self):
        print("credit card")

    def change_passwd(self):
        print("change password")


# create instance of class banking software
obj = banksoftware()

# get the input from the customer
x = input("Please select an option from the banking system: ")
if x == "cash":
    obj.cash_withdraw()
elif x == "credit":
    obj.credit_card()
elif x == "password":
    obj.change_passwd()
else:
    print("Option does not exist")


# 6. Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line


def multiplesof7():
    i = ''
    for x in range(2000, 3200):
        if x % 7 == 0 and x % 5 != 0:
            i = i + ", " + str(x)
    print(i)


multiplesof7()


# 7.Write a program which can compute the factorial of a given numbers.
# Use recursion to find it.
def factorial(data):
    k = data
    for i in range(1, data):
        k = k * i
    print(k)


factorial(8)

# 8.Write a program that calculates and prints the value according to the given formula
# :Q = Square root of [(2 * C * D)/H]Following are the fixed values of C and H: C is 50.
# H is 30.D  is  the  variable  whose  values  should  be  input  to  your  program
# in  a  comma-separated sequence.
# Example:Let  us  assume  the  following  comma  separated  input  sequence  is
# given  to  the program:100,150,180
# The output of the program should be:18,22,24

import math


def formula(*r):
    list_ans = ''
    for i in r:
        answer = math.sqrt((2 * 50 * i) / 30)
        list_ans = list_ans + ", " + str(int(answer))
    print(list_ans)


formula(100, 150, 180, 60)


# 9. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡-Y-1.

def twodimensionalarray(x, y):
    n = []
    for i in range(0, x):
        a_i = []  # iterate array
        for j in range(0, y):
            m = i * j
            a_i.append(m)
        n.append(a_i)
    print(n)


twodimensionalarray(3, 5)


# 10.Write a program that accepts a comma separated sequence of words as input
# and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,worldThen, the output should be:bag,hello,without,world

def inputFunction(*a):
    p = []
    oo = ''
    for k in a:
        p.append(str(k))
    bb = sorted(p)

    for jj in bb:
        oo = oo + ', ' + jj
    print(oo)


inputFunction(23, 43, 't', 'y', 'u', 'a', 'o', 9000, 9, 1, 'q', 'b', 'ppo', 'aa', 'without', 'hello', 'bag', 'world')


# 11. Write a program that accepts sequence of lines as input and
# prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:HELLO WORLD PRACTICE MAKES PERFECT


def lines(h):
    j = h.splitlines()
    n = []
    m = ''
    for i in range(len(j)):
        p = str.upper(j[i])  # capitalise each word
        a_i = p.split()
        n.append(a_i)
    my_list = ['\n' if i == [] else i for i in n]
    for a in range(len(my_list)):
        for y in my_list[a]:
            m = m + " " + y
    print(m)


lines('''particular king\n
there are your name''')


# 12. Write a program that accepts a sequence of whitespace separated words as input
# and   prints   the   words   after   removing   all   duplicate   words   and   sorting
# them alphanumerically. Suppose the following input is supplied to the program
# :hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

def updateinput(h):
    m = set(h.split())
    print(sorted(m))


updateinput('''here is where he lay as he waited for love and respect''')

# 13.Write  a  program  which  accepts  a  sequence  of  comma  separated  4  digit  binary
# numbers  as  its  input  and  then  check  whether  they  are  divisible  by  5  or  not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.


k = 1001, 0o110, 1010, 0o001


def divibinary(k):
    for var in k:
        if var % 5 == 0:
            print(var)
        else:
            pass


divibinary(k)

# 14.Write  a  program  that  accepts  a  sentence  and  calculate the  number  of  upper  case letters and lower
# case letters. Suppose the following input is supplied to the program: Hello world!Then, the output should be: UPPER
# CASE 1 LOWER CASE 9


m = '''YOu are a star'''
upper_k = 0
lower_k = 0
n = list(m)  # break it down to each character
print(n)
for var in n:
    if var.isupper():
        upper_k += 1
    else:
        lower_k += 1

print("LOWER CASE " + str(lower_k))
print("UPPER CASE " + str(upper_k))

# 15.Give example of fsum and sum function of math library.
import math

p = [2, 3, 4, 5]
k = math.fsum(p) # produces float output and is a method in the math module
print(k)

x = sum(p) # is an in built function
print(x)
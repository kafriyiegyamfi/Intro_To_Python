#!/usr/bin/python
i = 8
if(i % 2 == 0):
    print ("Even Number")
else:
    print ("Odd Number")

#% means modulus
# i%2 ==0 means a number is even

def evens(set):
    total=0
    for el in set:
        if el%2==0:
            total+=el
    return total

som=[1,2,3,4]
evens(som)

def get_age():
    age =int( input("please enter your age"))
    if (age>=45):
        print('you are old')
    else:
        print('you are young')

get_age()

def find_age():
    yob=int(input('enter your year of birth'))
    age=2019-yob
    print("you are ",age,'years old' )
    
    
find_age()

def leapYear():
    yob=int(input('enter your year of birth'))
    if yob%4==0:
        return True
    return False

leapYear()


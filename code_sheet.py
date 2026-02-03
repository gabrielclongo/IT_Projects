#Operations

#1

anything = input("Enter a number:")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

anything = input("Enter a number:")
something = int(anything) ** 2.0
print(anything, "to the power of 2 is", something)

anything = input("Enter a number:")
something = float(anything) ** 2.0
print(anything, "to the power of 2 is", something)

#2 (Converter)

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#Structure

print("+353" , "8923" , "12811", sep=' ')
print("+353" , "8923" , "12811", sep='-')
print("+353" , "8923" , "12811", sep=',')

print("i'm\nlearning\npython")
print("i'm\'learning\'python")
print("i am", "learning", "python")
print("i am learning" , "python" , end=" ")

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)
print(account_balance)
print(client_name)

name = 'Gabriel'
age = '19 years old'
height = 1.82 
print(name, age, height)

if height<2:
    print('Gabriel is short')
else:
    print('Gabriel is tall')

var = "3.8.5"
print("Python version: " + var)
var = 100
var = 200 + 300 
print(var)

a = 3.0
b = 4.0
c = (a**2 + b**2)**0.5
print(c)

John = 3
Mary = 5
Adam = 6
print(John, Mary, Adam, sep= ",")
total_apples = John + Mary + Adam 
print(total_apples)
print("Total number of apples:", total_apples)


#Input

name = input("What is your name?")
print("Hello," + name + "!!")

age = input("What is your age?")
print(age)

height = input("What is your height?")
print(height)

nationality = input("What is your nationality?")
print(nationality)

#Looping (Guess the right number until you get it)

#1

right_number = 500
guess_number = 50

while right_number != guess_number:
    guess_number = int(input("Enter a digit: "))
if right_number == guess_number:
    print("Good job! You are in.")
else:
    print("Wrong digit! Try again")   

 #2   

secret_number = 777
guess_number = 0
counter = 0
while guess_number != secret_number:
    guess_number = int(input("Enter an integer number: "))
    counter += 1
    if (guess_number == secret_number):
        print("Well done, muggle! You are free now.")
    else:
        print("Ha Ha! You are stuck in my loop!")
    
print("Number of attempts is: ", counter)  

#3

moneyInMypocket = 100.
while moneyInMypocket > 7.0: #when you can't afford it anymore
    #ask what drink your friend wants and how much
    #print("Buy a pint of Guinness")
    adrink = input("What do you want to drink:")
    drinkPrice = float(input("How much is it:"))
    if moneyInMypocket >= drinkPrice:
        moneyInMypocket -= drinkPrice
        print("here is your drink, ", adrink)
    else:
        print("The drink you want is too expensive, choose something cheaper!")
    moneyInMypocket -= drinkPrice


    print("The amount of money left is: ", moneyInMypocket)

 #4

MoneyInMypocket = 100.
if MoneyInMypocket > 7.0:
    print("Buy a pint of Guinness")
    moneyInMypocket -= 7.0 #moneyInMypocket = moneyInMypocket - 7.0

    print("The amount of money left is: ", moneyInMypocket)
    print("Now i am happy, i will go home")   


#Looping (Importing time) 

import time

for i in range(1, 6):
    print(i, "Mississipi")
    time. sleep(2)
print("Ready or not, here i come")
   
#Calculator

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

operation = input("choose operation (+, -, *, /):")
if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    print("Result:", num1 / num2)
else:
    print("Invalid operation")

#Function len()

numbers = [1, 2, 3, 4, 5]
numbers[len(numbers)//2] = int(input("Enter a new number: ")) #calculates the middle index
del numbers[len(numbers)-1] #delete the last one
print(len(numbers))
print(numbers)

hatList = [1, 2, 3, 4, 5]
hatList [2] = int(input("Enter the number you want to replace the middle number: "))
del hatList [4]
print("The list has", len(hatList), "numbers, ")
print(hatList)

#Adding elements to a list: append()
 
numbers[1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

#append() vs insert()

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)
###
numbers.append(4)
print(len(numbers))
print(numbers)
###
numbers.insert(0, 222)
print(len(numbers))
print(numbers)

my_list = []
for i in range(5):
    my_list.insert(0, i + 1)
print(my_list)    
#1-[]
#2-[1]
#3-[2, 1]
#4-[3,2,1]

beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrisson")

#Example 

for i in range (2): #in order to add two other names
    beatles.append(input("input the name: "))

del beatles[-1] #in order to delete the last element
del beatles[-1] #in order to delete the last element

beatles.insert(0, "Ringo Star") #in order to add "Ringo Star"

#List (Function)

my_list = [1, None, True, 'I am a string', 256, 0]
print[my_list[3]] #outputs: I am a string
print[my_list[-1]] #outputs: 0

#List (Method)

my_list[1] = '?'
print(my_list) #outputs: [1, '?', True, 'I am a string', 256, 0]

my_list.insert(0, "first") #That means you are addind an element to the list

#list (colors)

my_list = ["White", "Purple", "Blue", "Yellow", "Green"]
for i in range(5):
    print(my_list[i])

my_list = ["White", "Purple", "Blue", "Yellow", "Green", "Red"]
for i in range(5):
    print(my_list[i])

#In order to include "Red" to the list: change the number in range to 6

my_list = ["White", "Purple", "Blue", "Yellow", "Green", "Red"]
for i in range(6):
    print(my_list[i])   

#What is the output of the following snippett?

lst = [1, 2, 3, 4, 5]
lst.insert (1, 6)
del lst[0]
lst.append(1)

print(lst)
#output = [6, 2, 3, 4, 5, 1]


lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in list:
    add += number
    lst_2.append(add)

print(lst_2)  

#Sorting 

lst = [8, 10, 6, 2, 4]
sorted_list = sorted(lst, reverse=True)
print(sorted_list)

#The inner life of lists



#Powerful slices

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list) 

#
sum=0
for i in range(10):
    sum=sum+1
print(sum)    

sum = 0
for i in range(1, 11):
    #print(i)
    sum = sum + 1
print("The sum between 1 and 10 is: ", sum)

sum = 0
for i in range (1, 31):
    sum = sum + 1
print(sum)    

sum = 0
for i in range (1, 51):
    sum = sum + 1
print(sum)  

#CLASSES / OBJECTS

class Cat: 
    def __init__ (self, name, color):
        self.name = name
        self.color = color

cat1 = Cat("Tom", "black")
cat2 = Cat("Bob", "white")
cat3 = Cat("Rob", "brown")

print(cat1.name + " is " + cat1.color)
print(cat2,name + " is " + cat2.color)

# Vehicle: Speed, Mileage, Capacity
# Land Vehicle: Speed, Mileage, Capacity, SOE, Surface
# Wheeled Vehicle: Speed, Mileage, Capacity, SOE, Surface, Number of wheels

class vehicle:
    def __init__ (self, name, speed, color, capacity, mileage):
        self.name = name
        self.speed = speed
        self.color = color
        self.capacity = capacity
        self.mileage = mileage

    def set_engine (self, engine):
        self.engine = engine

vehicle1 = vehicle ("car", 120, "red", 5, 15)
vehicle1.set_engine ("v8")
LandVehicle1 = LandVehicle ("car", 120, "red", 5, 15, "road")
print(LandVehicle1)


class Star:
    def __init__ (self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__ (self):
        return self.name + ' in ' + self.galaxy

sun = Star("Sun", "Milky Way")
print(sun)
print(sun.name + " is in " + sun.galaxy)   

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Makes a sound"

# Child class
class Dog(Animal):
    def speak(self):
        return self.name + " says Woof!"

# Another child class
class Cat(Animal):
    def speak(self):
        return self.name + " says Meow!"

# Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())     # Buddy says Woof!
print(cat.speak())     # Whiskers says Meow!



class Person:
    def __init__(self,  name, age):
        self.name = name
        self.age = age
p1 = Person("Gabriel", 25)
print(p1.name)
print(p1.age)        

#Convertion

def celsius_to_fahreinheit(celsius):
        fahreinheit = (celsius * 9/5) + 32
        return fahreinheit

temp_c = 25
temp_f = celsius_to_fahreinheit(temp_c)
print (f"{temp_c} Celsius is {temp_f} fahreinheit")  

#Inheritance Structure:

class sports:
    pass
class leg_sports(sports):
    pass
class football(leg_sports(sports)):
    pass
class athletism(leg_sports(sports)):
    pass
class arm_sports(sports):
    pass
class basketball(arm_sports(sports)):
    pass
class handball(arm_sports(sports)):
    pass

#Counting instances of a class:

class User:
    count = 0

    def __init__(self.name):
        self.name = name
        User.count += 1
        print(f"Hello, i am {self.name}!")

    def greet(self):
        print(f"Hello, i am`{self.name}!") 

user1 = User("Alice")
user2 = User("Bob")
user3 = User("Charlie")

user1.greet()
user2.greet()
user3.greet()

print("Total users created:", User.count)

#Square Roots

import math

x = float(input("Enter x: "))
y = math.sqrt(x)

print("The square root of", x, "is equal to", y)

#Operations 

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

try:
    print(first_number / second_number)
except:
    print("This operation cannot be done.")    

print("THE END.")    

#Bank Account System

balance = 1000  # Starting balance

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Choose 1, 2 or 3: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print(f"New balance: {balance}")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Not enough money!")
        else:
            balance -= amount
            print(f"New balance: {balance}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
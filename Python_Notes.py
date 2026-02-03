#1- Define:

#Method: A method is a function defined inside a class that operates on instances of that class (i.e., objects). It defines the behavior of the objects.

#EX: 
class Calculator:
    def add(self, a, b):
        return a + b
    
calc = Calculator()
print(calc.add(10, 5)) 

#Constructor: A constructor is a special method that automatically runs when you create a new object from a class. Its job is to set up the object with initial values.

#EX: 
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

my_book = Book("1984", "George Orwell")
print(my_book.title)

#Abstraction: Abstraction is the process of hiding complex implementation details and showing only the essential features of the object.

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCard(PaymentMethod):   
        def process_payment(self, amount): 
            print(f"Processing ${amount} via credit card.")

payment = CreditCard()
payment.process_payment(100) 

#Inheritance: Inheritance allows a class (child or subclass) to inherit properties and methods from another class (parent or superclass).

class Animal:
     def speak(self):
          print("Animal makes a sound")

class Dog(Animal):
     def speak(self):
          print("Dog barks")         

pet = Dog() 
pet.speak()         

#Polymorphism: Polymorphism allows different classes to be treated through the same interface, typically by using methods with the same name but different implementations.

class Bird:
     def make_sound(self):
          print("Tweet")

class Cat:
     def make_sound(self):
          print("Meow")

def animal_sound(animal):
     animal.make_sound() 

animal_sound(Bird())     
animal_sound(Cat())                   

#2- Consider the following scenario:

#An online Pet Adoption System manages pets and adopters.

#Each pet has a name, type (e.g., dog, cat), and age.

#An adopter has a name and a unique ID.

#An adopter can adopt multiple pets.

#Tasks:
#a) Create a Python class called Pet. (5 Marks)
#b) Create a class called Adopter. (5 Marks)
#c) Implement a method in Adopter to adopt a pet. (5 Marks)

class Pet:
     def __init__(self, name, pet_type, age):
          self.name = name
          self.pet_type = pet_type
          self.age = age

     def __str__(self):
          return f"{self.pet_type.title()} named {self.name}, {self.age} years old"

class Adopter:
     def __init__(self, name, adopter_id):
          self.name = name
          self.adopter_id = adopter_id
          self.pets = []

     def adopt_pet(self, pet):
        self.pets.append(pet)
        print(f"{self.name} has adopted {pet.name}.")

     def show_adopted_pets(self):
          print(f"{self.name} has adopted the following pets:")
          for pet in self.pets:
               print(f" - {pet}") 

pet1 = Pet("Buddy", "dog", 3) 
pet2 = Pet("Mittens", "cat", 2)    

adopter1 = Adopter("Alice", "A001")
adopter1.adopt_pet(pet1)
adopter1.adopt_pet(pet2)
adopter1.show_adopted_pets()

#3- Explain the use of with open() in Python. How is it better than traditional open() and close()? 

#In Python, with open() is used to open a file, work with it, and automatically close it when you're done — even if an error occurs during file operations.
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
#with open() automatically closes the file when the block ends — even if there's an error.
#With open(), you must call close() manually, and it may be skipped if an exception occurs.

#Create and open a file called pets.txt in write mode and write three pet names:

# Writing to the file
with open("pets.txt", "w") as file:
    file.write("Buddy\n")
    file.write("Mittens\n")
    file.write("Goldie\n")
#Modify the program to read the file and count the number of lines:

# Reading from the file and counting lines
with open("pets.txt", "r") as file:
    lines = file.readlines()
    line_count = len(lines)

print(f"Number of pets listed: {line_count}")

#4- Explain how try-except-else-finally blocks work in Python. Provide a use case:

#In Python, the try-except-else-finally block is used for error handling. Each part has a specific role.

import math

def get_square_root():
    try:
        num = float(input("Enter a nuber: "))
        if num < 0:
             raise ValueError("Cannot take square root of a negative number.")
        result = math.sqrt(num)
    except ValueError as e:
         print(f"Error: {e}")
    else:
         print(f"The square root of {num} is {result:.2f}")

get_square_root()

#5- a) What are the differences between the math and random modules? Provide one example use of each.
   #b) Why is it considered good practice to import specific functions rather than entire modules? 
#math: provides mathematical functions and it is useful for calculations.
#random: generates random numbers and choices and it is useful for simulations, games and shuffling.

import math

print(math.sqrt(25))

import random

print(random.randint(1, 6))

#It is important to import specific functions instead of entire modules because it improves readability (it makes it clear what functions your code depends on), saves memory (as it only loads the required parts) and improves performance.

#Write a Python program using the datetime module to:
#Display the current date and time.
#Add 7 days to the current date and display the new date. 

from datetime import datetime, timedelta

current_datetime = datetime.now()
print("Current date and time:", current_datetime)

new_datetime = current_datetime + timedelta(days=7)
print("Date after 7 days:", new_datetime.date())

#What is the purpose of the sys module in Python? Provide two examples:

#The sys module provides access to system-specific parameters and functions, allowing you to interact with the Python interpreter and the command-line environment.

#Often used for:
#Working with command-line arguments
#Accessing the Python path, version info, etc.

#6- Mini Banking System:

def banking_system():
    balance = 1000  # Starting balance

    while True:
        print("\n--- Banking Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    balance += amount
                    print(f"✅ Deposit successful. New balance: ${balance:.2f}")
                else:
                    print("❌ Please enter a positive amount.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= balance and amount > 0:
                    balance -= amount
                    print(f"✅ Withdrawal successful. New balance: ${balance:.2f}")
                elif amount <= 0:
                    print("❌ Please enter a positive amount.")
                else:
                    print("❌ Insufficient funds.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

        elif choice == "3":
            print("👋 Thank you for using our banking system. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

# Run the program
banking_system()

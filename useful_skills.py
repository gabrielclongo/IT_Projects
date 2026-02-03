#How to use datetime


from datetime import datetime

today = datetime.now()

print(today.day, "/",  today.month, "/", today.year)


#How to define a number (even/odd)


number_definer = int(input("Enter a number: "))

if number_definer % 2 == 0:
    print(number_definer, "is even")
else:
    print(number_definer, "is odd")    


#How to code a dice


import random 

roll = random.randint(1,6)

print("Result =", roll)


#Guess the number game (Using try and handling errors)

secret_number = 505
attempts = 3

while attempts > 0:
    try:
        guess_number = int(input("Guess the number: "))
        if guess_number == secret_number:
            print("Correct!!")
            break
        else:
            attempts -= 1
            print(f"Not quite...{attempts} Attepts left")

    except ValueError:
        print("Enter a valid number")        

if attempts == 0:
    print("The secret number was", secret_number, "You're out")    


#Coding a menu with 3 options

while True:

    print("\n1. Hello")
    print("2. Bye")
    print("3. Exit")

    choice = input("Select an option, please: ")
    
    if choice == "1":
        print("Hey there!")
    elif choice == "2":
        print("Have a good one!")
    elif choice == "3":
        print("You're out")   
        break 

#List basics

numbers = [3, 7, 2, 9, 4]

print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Largest:", max(numbers))


#Defining a function and returning a value

def add(a,b):
    return a + b
result = add(15,5)
print("Result: ", result)

#Git commands

#cd path
#ls 
#git init
#git add (folder + "/")
#git add .
#git commit -m "Initial commit"
#git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
#git branch -M main
#git push -u origin main
#cd .. # goes back 



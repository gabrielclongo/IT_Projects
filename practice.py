print("Enter a number and it will say whether it is Even or Odd")

while True:
    try:
        number_definer = int(input("Enter a number: "))
    except ValueError:    
        print("Please enter a valid number.")
        continue

    if number_definer % 2 == 0:
        print(f"{number_definer} is Even!")
    else:
        print(f"{number_definer} is Odd!")    
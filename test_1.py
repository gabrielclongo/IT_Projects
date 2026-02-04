right_number = 505
attempts = 3

while attempts > 0:
    guess_number = int(input("Enter a number: "))

    if guess_number == right_number:
        print("Correct!")
        break
    else:
        attempts -= 1
        print(f"Wrong number!, {attempts} attempts left.")

if attempts == 0:
    print("You've been blocked!")        
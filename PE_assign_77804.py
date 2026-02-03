import json #Jaon offers tools so that we can read and write JSON files
from datetime import datetime #This will track rental start and end times 
from tabulate import tabulate #This reshapes the table containing the information

BIKES_FILE = 'bikes.json'
RENTALS_FILE = 'rentals.json' 
#Where the data will be saved

class Bike:
    def __init__(self, bike_id, model, available=True):
        self.bike_id = bike_id
        self.model = model
        self.available = available

    def to_dict(self):
        return {
            'bike_id': self.bike_id,
            'model': self.model,
            'available': self.available
        }

    @staticmethod
    def from_dict(data):
        return Bike(data['bike_id'], data['model'], data['available'])
#It will convert a dictionary JSON back into an object 

class Rental:
    def __init__(self, customer_name, bike_id, start_time):
        self.customer_name = customer_name
        self.bike_id = bike_id
        self.start_time = start_time  # datetime object

    def to_dict(self):
        return {
            'customer_name': self.customer_name,
            'bike_id': self.bike_id,
            'start_time': self.start_time.isoformat()
        }

    @staticmethod
    def from_dict(data):
        return Rental(data['customer_name'], data['bike_id'], datetime.fromisoformat(data['start_time']))

# Load bikes and rentals straight from JSON
def load_data():
    try:
        with open(BIKES_FILE, 'r') as f:
            bikes_data = json.load(f)
            bikes = [Bike.from_dict(b) for b in bikes_data]
    except FileNotFoundError:
        bikes = [
            Bike("B001", "Mountain Style"),
            Bike("B002", "City Style"),
            Bike("B003", "Electric")
        ]

    try:
        with open(RENTALS_FILE, 'r') as f:
            rentals_data = json.load(f)
            rentals = [Rental.from_dict(r) for r in rentals_data]
    except FileNotFoundError:
        rentals = []

    return bikes, rentals

def save_data():
    with open(BIKES_FILE, 'w') as f:
        json.dump([bike.to_dict() for bike in bikes], f, indent=2)

    with open(RENTALS_FILE, 'w') as f:
        json.dump([rental.to_dict() for rental in rentals], f, indent=2)


def show_bikes():
    print("\nAvailable Bikes:")
    table = []
    for bike in bikes:
        status = "Yes" if bike.available else "No"
        table.append([bike.bike_id, bike.model, status])
    print(tabulate(table, headers=["Bike ID", "Model", "Available"], tablefmt="grid"))


def rent_bike():
    bike_id = input("Enter the bike ID to rent: ").strip()
    for bike in bikes:
        if bike.bike_id == bike_id:
            if bike.available:
                name = input("Enter your name: ").strip()
                time = datetime.now()
                rentals.append(Rental(name, bike.bike_id, time))
                bike.available = False
                save_data()
                print("Bike rented.")
                return
            else:
                print("Bike not available.")
                return
    print("Bike not found.")

def return_bike():
    bike_id = input("Enter the bike ID to return: ").strip()
    for rental in rentals:
        if rental.bike_id == bike_id:
            for bike in bikes:
                if bike.bike_id == bike_id and not bike.available:
                    end_time = datetime.now()
                    duration = int((end_time - rental.start_time).total_seconds() // 60)
                    cost = duration * 0.1
                    bike.available = True
                    save_data()
                    print(f"Thank you! Bike returned. Duration: {duration} minutes. Cost: €{round(cost, 2)}")
                    return
    print("No available rental found.")

# Main Menu
def main():
    global bikes, rentals
    bikes, rentals = load_data()

    while True:
        print("\n1. Show Bikes\n2. Rent Bike\n3. Return Bike\n4. Exit")
        choice = input("Select an option: ").strip()
        if choice == "1":
            show_bikes()
        elif choice == "2":
            rent_bike()
        elif choice == "3":
            return_bike()
        elif choice == "4":
            print("Thank you for choosing us! See you next time.")
            break
        else:
            print("Invalid option.")

main()

#When running the code, four options will be displayed:

#1. It will show you the bikes - Expected output = Table showing the Bike ID, model and availability.
#2. It will let you rent a bike - Expected output = "Enter the bike ID to rent:", "Enter your name:", "Bike rented"
#3. It will let you return your bike - Expected output = "Enter the bike ID to return:", "Thank you! Bike returned. Duration: x. Cost: x"
#4. It will let you exit - Expected output = "Thank you for choosing us! See you next time."

#When entering the wrong bike id: - Expected output = "Bike not found."

#Example:

#Select an option: 1 - Expected output = Table
#Select an option: 2 - Expected output = Enter the bike ID to rent: B002 - Enter your name: Gabriel - Bike rented.
#Select an option: 3 - Expected output = Enter the bike ID to return: B002 - Thank you! Bike returned. Duration: 36 minutes. Cost: €3.6
#Select an option: 4 - Expected output = Thank you for choosing us! See you next time.

#Example: 

#Select an option: 1 - Expected output = Table
#Select an option: 2 - Expected output = Enter the bike ID to rent: b002 - Bike not found. - Select an option:


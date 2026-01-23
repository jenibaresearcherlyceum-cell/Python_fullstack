def add_number(numbers):
    n = int(input("Enter number: "))
    numbers.append(n)
    print("Number added")

def view_numbers(numbers):
    print("Numbers:", numbers)

def calculate_sum(numbers):
    print("Sum:", sum(numbers))

numbers = []

while True:
    print("\nMENU")
    print("1. Add number")
    print("2. View numbers")
    print("3. Calculate sum")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_number(numbers)
    elif choice == 2:
        view_numbers(numbers)
    elif choice == 3:
        calculate_sum(numbers)
    elif choice == 4:
        print("Program exited")
        break
    else:
        print("Invalid choice")

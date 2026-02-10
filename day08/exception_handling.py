# 1.Safe Number Input

def get_valid_number():
    while True:
        try:
            number = int(input("Enter an integer: "))
            print("Valid number entered:", number)
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


# 2.Custom Exception

class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    else:
        print("Age is valid.")


# 3.File Error Handling

def open_file():
    try:
        file = open("sample.txt", "r")
        content = file.read()
        print(content)
        file.close()
    except FileNotFoundError:
        print("File not found. Please check the file name.")


# Main Execution

if __name__ == "__main__":
    
    print("\n--- 1.Safe Number Input ---")
    get_valid_number()

    print("\n--- 2.Custom Exception ---")
    try:
        age = int(input("Enter your age: "))
        check_age(age)
    except InvalidAgeError as e:
        print("Custom Exception Caught:", e)
    except ValueError:
        print("Please enter a valid number for age.")

    print("\n--- 3.File Error Handling ---")
    open_file()

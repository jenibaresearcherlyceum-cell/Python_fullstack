while True:
    age_input = input("enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter a valid number for age.")

if age > 60:
    print("senior citizen")

elif age >= 18:
    print("eligible")

else:
    print("not eligible")

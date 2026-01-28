name = input("Enter your name: ")
city = input("Enter your city: ")

file = open("data.txt", "w")
file.write("Name: " + name + "\n")
file.write("City: " + city)
file.close()

file = open("data.txt", "r")
content = file.read()
print("\nFile Content:")
print(content)
file.close()

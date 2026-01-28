name = input("Enter student name: ")
course = input("Enter course: ")
marks = input("Enter marks: ")

file = open("students.txt", "a")
file.write("Name: " + name + ", Course: " + course + ", Marks: " + marks + "\n")
file.close()

file = open("students.txt", "r")
print("\nAll Students Data:")
print(file.read())
file.close()

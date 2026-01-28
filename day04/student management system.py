import json

FILE_NAME = "students.json"

def load_students():
    try:
        file = open(FILE_NAME, "r")
        data = json.load(file)
        file.close()
        return data
    except:
        return {}

def save_students(students):
    file = open(FILE_NAME, "w")
    json.dump(students, file)
    file.close()

students = load_students()

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    students[sid] = {
        "Name": name,
        "Course": course,
        "Marks": marks
    }

    save_students(students)
    print("Student added successfully")

def view_students():
    if not students:
        print("No students found")
    else:
        for sid, details in students.items():
            print("\nID:", sid)
            print("Name:", details["Name"])
            print("Course:", details["Course"])
            print("Marks:", details["Marks"])

def search_student():
    sid = input("Enter Student ID to search: ")
    if sid in students:
        details = students[sid]
        print("Name:", details["Name"])
        print("Course:", details["Course"])
        print("Marks:", details["Marks"])
    else:
        print("Student not found")
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting program")
        break
    else:
        print("Invalid choice")

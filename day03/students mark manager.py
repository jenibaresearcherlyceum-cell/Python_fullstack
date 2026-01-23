def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

name = input("Enter student name: ")
marks = []

for i in range(5):
    m = int(input("Enter mark: "))
    marks.append(m)

total = calculate_total(marks)
average = calculate_average(marks)
grade = calculate_grade(average)

print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)

def find_sum(numbers):
    return sum(numbers)

def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def average(numbers):
    return sum(numbers) / len(numbers)

count = int(input("How many numbers? "))
numbers = []

for i in range(count):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Sum:", find_sum(numbers))
print("Maximum:", find_max(numbers))
print("Minimum:", find_min(numbers))
print("Average:", average(numbers))

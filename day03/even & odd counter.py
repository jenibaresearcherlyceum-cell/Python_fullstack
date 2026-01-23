def count_even_odd(numbers):
    even = 0
    odd = 0

    for num in numbers:
        if num % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1

    return even, odd

numbers = []
count = int(input("How many numbers? "))

for i in range(count):
    n = int(input("Enter number: "))
    numbers.append(n)

even_count, odd_count = count_even_odd(numbers)

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

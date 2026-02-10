 Day 08 – Exception Handling

Task A1 – Safe Number Input:
      ->Used try–except to repeatedly ask for integer input until valid.

Task A2 – Custom Exception:
      ->Created a custom exception called InvalidAgeError.
      ->Raised error if age is below 18.

Task A3 – File Error Handling:
      ->Handled FileNotFoundError when trying to open a         non-existing file.

Concepts Used
- try
- except
- while loop
- custom exception
- File handling

1. What is an Exception:
     An exception is an error that occurs during the execution of a program.

Examples:
   ->Invalid user input
   ->Dividing by zero
   ->File not found
 If exceptions are not handled, the program will crash.

2. try – except

i) try Block:
    ->The try block contains code that may cause an error.

ii)except Block:
    ->The except block handles the error and prevents the program from crashing.

Syntax:
try:
    # risky code
except ErrorType:
    # handling code

 Example:
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a number.")


If the user enters text instead of a number,
ValueError is handled.

3. Why Do We Use Exception Handling?

   ->To prevent program crash

   ->To handle errors properly

   ->To make the program user-friendly

   ->To control unexpected situations

4. Custom Exception:

    ->Python has built-in exceptions like:

    i)ValueError

    ii)TypeError

    iii)FileNotFoundError

 ->But sometimes we need our own rule-based errors.

 ->A Custom Exception is a user-defined exception created by inheriting from the Exception class.

 Syntax:
class ErrorName(Exception):
    pass

Example:
class InvalidAgeError(Exception):
    pass

age = 15

if age < 18:
    raise InvalidAgeError("Age must be 18 or above")

5.raise Keyword:

  ->The raise keyword is used to manually generate an exception.

Example:
    raise ValueError("Invalid value")

6. FileNotFoundError:

   ->This is a built-in exception.

   ->It occurs when we try to open a file that does not exist.

Example:

try:
    file = open("sample.txt", "r")
except FileNotFoundError:
    print("File not found.")

Summary of Day08:

    ->try is used for risky code

    ->except handles the error

    ->raise generates an exception

    ->Custom exception inherits from Exception

    ->FileNotFoundError is a built-in exception

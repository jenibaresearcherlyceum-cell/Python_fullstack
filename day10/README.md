# Day 10 – Refactoring Practice

## What is Refactoring?:
    ->Refactoring means improving the internal structure of code without changing its output.

    ->It makes code:
        - Clean
        - Readable
        - Reusable
        - Professional
## DRY Principle:
    ->DRY means “Don’t Repeat Yourself”.
    ->We should avoid writing the same code multiple times.
    ->Instead, we create reusable functions.

## Function Decomposition:

    ->A long function should be divided into smaller functions.
    ->Small functions are easy to test and debug.

## Naming Conventions:

    ->Variables should have meaningful names.
    ->Class names use Capital letters.
    ->Function names use small letters with underscore.

Example:
-------
Wrong:
a = 10
-------
Correct:
employee_id = 10

## Code Readability:
        Code should be:
            ->Easy to read
            ->Properly formatted
            ->Clean and structured
            ->Not cluttered
            ->Refactoring makes the project look professional.

## Task1 – Refactor Long Function:

A long function was divided into:
- get_employee_input()
- is_duplicate()
- create_employee()
- add_employee_new()

This improves readability and reduces complexity.

---

## Task2 – Clean Naming:

Variables like:
a, b, x, y

Were renamed to:
employee_id, employee_name, employee_list, department_name

This improves clarity.

---

## Task3 – Remove Repeated Code:

Repeated save logic was moved into:

save_all_data()

This follows the DRY principle (Don't Repeat Yourself).

---

## Conclusion

Refactoring improves code quality without changing functionality.
It helps developers maintain and scale projects easily.

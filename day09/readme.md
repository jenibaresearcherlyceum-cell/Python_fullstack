DAY 09 — SEARCH, FILTER & REPORTING

1. Filtering Lists:
   ->Filtering allows us to extract specific elements from a list based on a condition.

   Example:

       Filtering employees by department (CSE only).

    Used:
        -> for loop
        ->if condition
        ->List comprehension

2. List Comprehension:
      ->A short and clean way to create a filtered list.

Syntax:
       new_list = [item for item in list if condition]

Used to:
       Extract CSE employees

3. Sorting Data:
       ->Sorting arranges data in a specific order.

Used:
    ->sorted() function
    ->lambda function

Examples:
       ->Sort employees by name
       ->Sort employees by salary

4. Lambda Function:
        ->A small anonymous function used mainly for sorting.

Example:
        lambda x: x["salary"]

5. Counting & Summary:
        -> Used counting logic to calculate:
        -> Assigned tasks
        -> In Progress tasks
        -> Completed tasks
        -> Also generated:
        -> Total employees
        -> Total tasks
        -> Department-wise summary


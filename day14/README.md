# Day 14 – Performance Thinking & Code Efficiency

## 1. What is Time Complexity?
        -->Time complexity means:
            How the running time of a program increases when data size increases.
            If data increase → time also increase.
        -->Basic Types:
            *O(1) → Constant time (very fast)
            *O(n) → Runs once for each item
            *O(n²) → Nested loop (slow for large data)
        -->Example:

            for emp in employees:
                print(emp.name)

        *This is O(n).

## 2. Why Nested Loops Slow Systems:
        -->Nested loops increase execution time significantly when data size grows.
        -->Example:
            for emp in employees:
                for task in tasks:
                    print(emp.name, task.title)

    -->If there are 100 employees and 100 tasks:
       100 × 100 = 10,000 iterations.

*This is O(n²).
*This reduces performance in large systems.


## 3. Efficient Searching Using Dictionary:
        -->Searching in a list takes O(n) time.
        -->Dictionary lookup takes O(1) time.

    -->Searching in list:

        for emp in employees:
         if emp.emp_id == 101:
            print(emp.name)

        *This takes O(n).

    -->Better method:

        employee_dict = {emp.emp_id: emp for emp in employees}
            print(employee_dict[101].name)

        *Dictionary lookup is O(1) → very fast.

    -->Example:
            *employee_dict = {emp.emp_id: emp}
            *Using dictionaries improves performance in large datasets.


## 4. Minimizing File I/O:
    -->Writing to a file multiple times slows down the system.
    -->Instead of saving after every small change,
       batch operations and save once.
    -->This improves efficiency.

-->Wrong way:

    add_employee()
    save_file()

    add_task()
    save_file()

    delete_task()
    save_file()

-->Correct Way:

    add_employee()
    add_employee()
    delete_employee()

    save_file()   # Only once


## 5. Memory vs Speed Tradeoff:
    -->Lists use less memory but are slower for searching.-->Dictionaries use more memory but provide faster access.

    -->Developers must balance memory usage and performance.


## Conclusion
    -->Performance thinking helps developers write efficient code.
    -->Optimizing loops, reducing unnecessary file writes,and using dictionaries for faster lookup improvessystem performance and scalability.

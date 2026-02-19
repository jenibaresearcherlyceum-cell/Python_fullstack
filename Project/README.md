# College Employee and Task Management System:

## Description:
  -->A Python-based modular system designed to manage college employees and track academic/administrative tasks efficiently.
  -->The system supports role-based access, secure data handling, logging, reporting, and optimized performance.

## Project Objective:
  -->Design a structured and scalable employee-task management system
  -->Implement JSON-based data persistence
  -->Integrate validation, logging, role-based access control
  -->Maintain professional code architecture
  -->Simulate a real-world administrative system

## Features:
 --> Employee Management (Add, View, Search, Delete)
 -->Task Assignment & Status Tracking
 -->Role-Based Access (Admin / Staff)
 -->Safe Deletion with Data Integrity
 -->Dashboard & Reports
 -->Search & Sorting
 -->Audit Logging
 -->Optimized Lookup Performance
 -->JSON Data Persistence
 -->Exception Handling & Validation

## Technologies Used:
         *Python
         *JSON File Handling
         *Logging Module
         *Object-Oriented Programming (OOP)
         *Git & GitHub

## How to Run:
   -->Clone the repository
   -->Navigate to the project folder
   -->Run: python main.py

### Daily Development Log:

## Day 1 – Project Initialization:
    -->Created project folder structure
    -->Created modules: employee.py, task.py, file_handler.py
    -->Defined Employee class with:
        * __init__()
        * to_dict()
        * display()
    -->Defined Task class with:
        * __init__()
        * update_status()
        * display_task()

    -->Created file handler skeleton:
        * save_data()
        * load_data()
        
Project structure and core class design completed.

## Day 2 – JSON Data Persistence:
    -->Added from_dict() methods in Employee and Task classes
    -->Implemented:
        * save_employees()
        * load_employees()
        * save_tasks()
        * load_tasks()

    -->Enabled JSON file storage
    -->Tested save and load workflow
    
Persistent data storage successfully implemented.

## Day 3 – Main Module Integration:
    -->Created main.py
    -->Implemented menu-driven loop
    -->Integrated employee and task modules
    -->Linked tasks using emp_id
    -->Added task status flow:
        * Assigned
        * In Progress
        * Completed
    -->Implemented load at startup and save on exit

System execution flow established.

## Day 4 – Validation & Stability:
    -->Prevented duplicate employee IDs
    -->Validated task assignment
    -->Added try–except for safe input handling
    -->Improved formatted output display
    -->Handled missing JSON files gracefully
    
System reliability improved.

## Day 5 – Search & Reporting:
    -->Implemented employee search (case-insensitive)
    -->Added task filtering by status
    -->Created employee task summary report
    -->Added system dashboard
    -->Implemented sorting options

Search and reporting module completed.

## Day 6 – Code Refactoring:
    -->Refactored main.py into modular functions
    -->Created reusable validation helpers
    -->Improved structured output formatting
    -->Added docstrings to modules and classes

Code structure optimized.

## Day 7 – Role-Based Access Control:
    -->Created auth.py
    -->Implemented login system
    -->Defined Admin and Staff roles
    -->Restricted menu based on role
    -->Implemented task ownership validation
    -->Limited login attempts

Access control system integrated.

## Day 8 – Safe Deletion & Data Management:
    -->Implemented employee deletion (Admin only)
    -->Implemented task deletion
    -->Added soft delete (is_active flag)
    -->Updated dashboard to show active/inactive employees
    -->Verified JSON integrity

Data management enhanced.

## Day 9 – Audit Logging:
    -->Created logger.py
    -->Configured centralized logging
    -->Logged login attempts
    -->Logged add/delete operations
    -->Logged unauthorized access
    -->Prevented logging sensitive data

Audit logging implemented.

## Day 10 – Optimization & Final Hardening:
    -->Optimized employee lookup using dictionary mapping
    -->Grouped tasks by employee
    -->Reduced redundant JSON writes
    -->Centralized save logic
    -->Strengthened error handling
    -->Cleaned unused code and ensured consistent formatting

System optimized and stabilized.



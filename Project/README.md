College Employee and Task Management System
Description
A Python-based modular system designed to manage college employees and track academic/administrative tasks efficiently. The system supports role-based access control, secure JSON data handling, logging, reporting, and performance optimization.
Project Objectives
-Design a structured and scalable employee–task management system
-Implement JSON-based data persistence
-Integrate validation, logging, and role-based access control
-Maintain professional and modular code architecture
-Simulate a real-world administrative system
Features
-Employee Management (Add, View, Search, Soft Delete)
-Task Assignment & Status Tracking
-Role-Based Access Control (Admin / Staff)
-Safe Deletion with Data Integrity
-Dashboard & Reporting System
-Search & Sorting Functionality
-Audit Logging
-Optimized Dictionary-Based Lookup
-JSON Data Persistence
-Exception Handling & Validation
Technologies Used
-Python
-JSON File Handling
-Logging Module
-Object-Oriented Programming (OOP)
-Git & GitHub
How to Run
-Clone the repository
-Navigate to the project folder
-Run the command: -python main.py
Daily Development Log
Day 1 – Project Initialization
-Created project folder structure
-Created modules: employee.py, task.py, file_handler.py
-Defined Employee class with:
  * __init__()

  * to_dict()

  * display()
-Defined Task class with:
  * __init__()

  * update_status()

  * display()
-Created file handler skeleton:
  * save_data()

  * load_data()
-Project structure and core class design completed.
Day 2 – JSON Data Persistence
-Added from_dict() methods in Employee and Task classes
-Implemented:
•	save_employees()
•	load_employees()
•	save_tasks()
•	load_tasks()
-Enabled JSON file storage
-Tested save and load workflow
-Persistent data storage successfully implemented.
Day 3 – Main Module Integration
-Created main.py
-Implemented menu-driven loop
-Integrated employee and task modules
-Linked tasks using emp_id
-Added task status flow:
* Assigned

* In Progress

* Completed
-Implemented load at startup and save on exit
-System execution flow established.
Day 4 – Validation & Stability
-Prevented duplicate employee IDs
-Validated task assignment
-Added try–except for safe input handling
-Improved formatted output display
-Handled missing JSON files gracefully
-System reliability improved.
Day 5 – Search & Reporting
-Implemented employee search (case-insensitive)
-Added task filtering by status
-Created employee task summary report
-Added system dashboard
-Implemented sorting options
-Search and reporting module completed.
Day 6 – Code Refactoring
-Refactored main.py into modular functions
-Created reusable validation helpers
-Improved structured output formatting
-Added docstrings to modules and classes
-Code structure optimized and improved for readability.
Day 7 – Role-Based Access Control
-Created auth.py
-Implemented login system
-Defined Admin and Staff roles
-Restricted menu based on role
-Implemented task ownership validation
-Limited login attempts
-Access control system successfully integrated.
Day 8 – Safe Deletion & Data Management
-Implemented employee deletion (Admin only)
-Implemented task deletion
-Added soft delete using is_active flag
-Updated dashboard to show active/inactive employees
-Verified JSON integrity and prevented orphan records
-Data consistency and safe deletion logic implemented.
Day 9 – Audit Logging
-Created logger.py
-Configured centralized logging system
-Logged login attempts
-Logged add/delete operations
-Logged unauthorized access attempts
-Avoided logging sensitive information (passwords)
-Audit logging system integrated.
Day 10 – Optimization & Performance Enhancement
-Optimized employee lookup using dictionary mapping
-Grouped tasks by employee for faster access
-Reduced redundant JSON write operations
-Centralized save logic
-Strengthened global error handling
-Removed unused code and ensured consistent formatting
-System performance and maintainability improved.
Day 11 – Final Stabilization & Project Freeze
-Performed full system audit
-Verified modular structure
-Ensured no duplicate save logic
-Checked unused imports and debug prints
-Confirmed proper role-based restrictions
-Verified logging and soft delete functionality
-Final folder cleanup completed
-Core functionality frozen for final submission.
Day 12 – Migration from JSON to SQLite Database
-Replaced JSON-based storage with SQLite database integration
-Created centralized database.py to handle DB connection and table creation
-Implemented automatic table initialization for employees and tasks
-Replaced file handler logic with INSERT and SELECT database operations
-Updated employee module to use database queries for add and view operations
-Updated task module to support INSERT, UPDATE, and SELECT queries
-Completely removed JSON dependency (employees.json, tasks.json)
-Ensured full data persistence after program restart
-Project successfully transitioned to database-driven architecture
Day 13 – Database Abstraction Layer (DAL) Implementation
-Centralized all SQL queries inside database.py
-Removed SQL statements from employee.py, task.py, and main.py
-Introduced clean Data Access Layer structure
-Optional service layer introduced for validation and business rules
-Established structured flow: main → service → database → SQLite
-Implemented safe connection handling using context manager with (sqlite3.connect)
-Improved maintainability and separation of concerns
-Verified full system functionality after architecture refactor
Day 14 – API Style Architecture Preparation
-Converted system logic to API-style structure
-Defined and documented REST-style endpoints in README
-Introduced controller layer for request handling
-Shifted flow to: main → controller → service → database
-Standardized response format for all operations (success/error structure)
-Implemented structured error handling mechanism
-Maintained console menu compatibility during backend preparation
-Backend successfully decoupled from UI layer
Day 15 – Flask Integration & API Server Initialization
-Installed and configured Flask within project environment
-Created app.py as backend entry point
-Initialized Flask application and root route
-Connected controllers to Flask routes
-Implemented first live GET API endpoint
-Implemented POST API using request.json for data handling
-Successfully started local Flask server
-Verified API endpoints via browser/Postman
-Preserved existing console-based system during transition
Day 16 – Full REST API Implementation & Testing
-Implemented complete CRUD APIs for Employees
-Implemented complete CRUD APIs for Tasks
-Integrated request handling using request.json
-Standardized API response structure (status, message, data)
-Implemented proper HTTP status codes (200, 201, 400, 404, etc.)
-Applied safe delete logic where required
-Completed structured error handling for invalid inputs and missing records
-Conducted full endpoint testing using Postman (GET, POST, PUT, DELETE)
-Achieved fully functional backend API service architecture
DAY 17 — AUTHENTICATION SYSTEM & PASSWORD SECURITY
•	Installed bcrypt for secure password hashing
•	Implemented password hashing during user registration
•	Added password verification during login process
•	Ensured passwords are stored as hashed values in database
•	Verified no plain text passwords stored
•	Prevented passwords from appearing in API responses
•	Confirmed passwords are not printed in system logs
•	Implemented basic API protection using login state
•	Restricted sensitive endpoints from unauthorized access
Security Verification:
•	Database shows hashed passwords (60 bytes bcrypt hash)
•	Logs do not expose password values
•	API responses do not contain password fields

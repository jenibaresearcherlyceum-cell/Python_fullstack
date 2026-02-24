Objective

The purpose of this module is to understand and implement Layered Software Architecture by separating:

- Presentation Layer

- Business Logic Layer

- Data Access Layer

This improves code maintainability, readability, and scalability.

Concepts Covered

 - Software Architecture

 - Separation of Concerns (SoC)

 - Layered Architecture Design

 - Avoiding SQL inside UI code

 - Writing reusable data access functions

 - Maintainable backend structure

Architecture Used

 - This project follows a 3-Layer Architecture:

    1. Presentation Layer (main.py)

        - Handles user input

        - Displays menu options

        - Calls service layer functions

        - Does NOT contain SQL queries

    2. Business Layer (service.py)

        - Contains business rules and validations

        - Calls database functions

        - Acts as a bridge between UI and database

        - No direct SQL written here

    3. Data Layer (database.py)

        - Handles SQLite connection

        - Executes SQL queries

        - Performs CRUD operations

        - No user input or print statements


Good Architecture Example

 - SQL queries moved to database.py

 - Business logic inside service.py

 - UI code inside main.py

 - Clean separation of concerns

 - Reusable data access functions

Features Implemented

 - Create Employee Table

 - Insert Employee

 - View All Employees

 - Update Employee

 - Delete Employee

 - Reusable get_all_employees() function

 - Proper Layer Separation

Technologies Used

 - Python

 - SQLite

 - Modular File Structure


Why This Architecture Is Better

 - Easy to debug

 - Easy to extend

 - Clean code structure

 - Professional backend design

 - Scalable for future improvements

Limitations

 - Console-based application

 - No authentication module

 - No advanced validation

 - Basic error handling only
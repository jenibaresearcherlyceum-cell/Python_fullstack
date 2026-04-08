# Day 16 – Relational Databases & SQL Basics

## Overview

In Day 16, the project was extended from file-based JSON storage to a relational database using SQLite.  
This helped in understanding how structured databases work and how SQL is used to manage data.

---

## 1. What is a Database?

A database is a structured system used to store and manage data efficiently.  
Unlike JSON files, databases allow faster querying, better organization, and scalability.

SQLite was used as it is lightweight, serverless, and built into Python.

---

## 2. JSON vs Database

JSON:
- File-based storage
- Suitable for small projects
- Manual read/write operations

Database:
- Structured table format
- Query-based access using SQL
- Efficient for large datasets
- Supports relationships between tables

---

## 3. Tables Created

Two tables were created:

### employees
- emp_id (Primary Key)
- name
- department
- designation

### tasks
- task_id (Primary Key)
- title
- emp_id (Foreign Key)
- status

Primary key ensures unique identification of each record.

---

## 4. SQL Operations Implemented (CRUD)

The following operations were implemented:

### Create
Inserted new employee records using INSERT.

### Read
Fetched all employees using SELECT.

### Update
Updated employee department using UPDATE.

### Delete
Deleted employee records using DELETE.

All queries were executed using parameterized SQL to improve security.

---

## 5. Key Concepts Learned

- Database fundamentals
- Tables, rows, columns
- Primary key and foreign key
- Basic SQL commands
- SQLite integration with Python
- CRUD operations
- Importance of commit() in saving changes

---

## Conclusion

This day introduced relational database concepts and SQL basics.  
The project now demonstrates how structured data storage works using SQLite, moving beyond JSON-based storage.

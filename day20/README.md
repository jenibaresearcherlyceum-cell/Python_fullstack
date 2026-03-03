## Day 20 – REST APIs & HTTP CRUD Operations

# Overview

This module implements a RESTful API using Flask to perform CRUD operations on employee resources. Proper HTTP methods and status codes are used.

# Learning Objectives

  -Understand RESTful API design

  -Map CRUD operations to HTTP methods

  -Handle JSON request body

  -Return structured JSON responses

  -Use proper HTTP status codes

  -Test APIs using Postman

# CRUD → HTTP Mapping

Operation	HTTP Method	Endpoint
Create Employee	POST	/employees
View Employees	GET	/employees
Update Employee	PUT	/employees/<id>
Delete Employee	DELETE	/employees/<id>

# Example JSON Request (POST)

{
  "name": "John",
  "department": "CSE"
}

# Example JSON Response

{
  "status": "success",
  "message": "Employee created",
  "data": {
    "id": 1,
    "name": "John",
    "department": "CSE"
  }
}

# HTTP Status Codes Used

200 → Success

201 → Resource Created

400 → Bad Request

404 → Not Found

500 → Server Error

# How to Run
pip install flask
python crud_api_practice.py


Open in Postman:

POST → http://127.0.0.1:5000/employees

GET → http://127.0.0.1:5000/employees
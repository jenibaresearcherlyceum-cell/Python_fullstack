##Task1 — Basic Logger

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")
print("Program executed successfully")

##Task A2 — Log User Actions
  
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def login(username, password):
    if username == "admin" and password == "1234":
        logging.info("Login success for user: " + username)
        print("Login Successful")
    else:
        logging.warning("Login failed for user: " + username)
        print("Login Failed")

def add_data():
    logging.info("Data added")

def delete_data():
    logging.info("Data deleted")

##Task A3 — Log Errors
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)

except Exception as e:
    logging.error(str(e))
    print("An error occurred")

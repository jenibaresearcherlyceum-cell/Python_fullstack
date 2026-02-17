# Day 13 – Logging & System Monitoring

## 1. What is Logging?
        -->Logging is the process of recording events that happen while a program is running.

        -->Instead of only displaying output on the screen, logging stores important information in a file.  
        -->This helps developers monitor system behavior and fix errors easily.

    Example:
        - Program started
        - User logged in
        - Data added or deleted
        - Error occurred

## 2. Audit Trail:
        -->An audit trail is a record of system activities that helps track user actions and changes.

## 3. Logging Module Functions:
        -->logging.debug()
        -->logging.info()
        -->logging.warning()
        -->logging.error()
        -->logging.critical()

## 4. Log Levels in Python:

        -->Python logging module provides different log levels to classify messages:

            - DEBUG – Detailed information for debugging
            - INFO – General information about normal program execution
            - WARNING – Something unexpected happened, but the program still runs
            - ERROR – A serious problem occurred
            - CRITICAL – A very serious error that may stop the program

        Example:
            *logging.info("Program started")
            *logging.warning("Low memory")
            *logging.error("File not found")


## 6. Difference Between print() and logging:

| print()                      | logging |
|------------------------------|----------|
| Displays output on the screen| Stores output in a file |
| Temporary                    | Permanent record |
| Used for simple debugging  | Used in real-world applications| 
| No log levels              |    Supports multiple log levels |

    -->print() is useful for testing.  
    -->logging is used in professional projects.


## 7. Why Logging is Important?
    -->Logging is important because:
        - It helps track errors
        - It records user actions (audit trail)
        - It improves system monitoring
        - It helps in debugging
        - It increases application security

    -->In real-world applications, logging is essential for maintaining and monitoring systems.
## 8. Format:
    "%(asctime)s - %(levelname)s - %(message)s"

        * asctime → Time
        * levelname → INFO/ERROR
        * message → Your message

## Conclusion:
    -->Logging helps developers understand what is happening inside the program.  
    -->It is an important tool for debugging, monitoring, and maintaining applications.

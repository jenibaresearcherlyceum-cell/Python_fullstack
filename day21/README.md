## Overview

This module introduces authentication concepts and demonstrates secure password handling using bcrypt hashing.

# Learning Objectives

  -Understand authentication vs authorization

  -Learn why plain-text passwords are insecure

  -Use bcrypt for password hashing

 -Implement secure login validation

  -Return structured authentication responses

# Key Concepts

    Authentication

        -Verifying user identity using credentials.

    Authorization

        -Determining what actions a user is allowed to perform.

# Why Not Plain-Text Passwords?

Storing passwords in plain text is insecure and vulnerable to data breaches.

# Password Hashing with bcrypt

bcrypt:

  -Automatically adds salt

  -Produces secure hash

  -Prevents password reversal

  -Industry standard for secure systems

# Example Hashing Code

import bcrypt

password = "mypassword".encode()
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

bcrypt.checkpw(password, hashed)

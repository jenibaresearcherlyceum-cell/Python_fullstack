<<<<<<< HEAD
## Day 22 – JWT Authentication & API Security

# Overview

This module introduces JWT (JSON Web Token) authentication and demonstrates how APIs implement secure token-based authentication.

# Learning Objectives

Understand token-based authentication

Learn why APIs use tokens instead of sessions

Generate JWT tokens

Verify tokens in API requests

Handle token expiration

# What is JWT?

JWT (JSON Web Token) is a secure method used for transmitting authentication information between client and server.

It is commonly used for stateless API authentication.

# JWT Structure

JWT consists of three parts:

Header:
       Defines algorithm

Payload:
        Contains Data

Signature:
        Used to verify token authenticity.

Example:

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# Token Authentication Flow

    User logs in.

    Server generates JWT token.

    Client stores token.

    Client sends token in request header.

    Server verifies token before granting access.

Example Token Generation

payload = {
 "user": "admin",
 "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
}

=======
## Day 22 – JWT Authentication & API Security

# Overview

This module introduces JWT (JSON Web Token) authentication and demonstrates how APIs implement secure token-based authentication.

# Learning Objectives

Understand token-based authentication

Learn why APIs use tokens instead of sessions

Generate JWT tokens

Verify tokens in API requests

Handle token expiration

# What is JWT?

JWT (JSON Web Token) is a secure method used for transmitting authentication information between client and server.

It is commonly used for stateless API authentication.

# JWT Structure

JWT consists of three parts:

Header:
       Defines algorithm

Payload:
        Contains Data

Signature:
        Used to verify token authenticity.

Example:

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# Token Authentication Flow

    User logs in.

    Server generates JWT token.

    Client stores token.

    Client sends token in request header.

    Server verifies token before granting access.

Example Token Generation

payload = {
 "user": "admin",
 "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
}

>>>>>>> 22031014cf25f8636d0293228d2970b67ec231f8
token = jwt.encode(payload, "secret_key", algorithm="HS256")
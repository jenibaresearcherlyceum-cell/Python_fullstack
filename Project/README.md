## Employee Management System
## Overview

This is a full stack Employee Management System built using Flask and React.
It supports secure authentication, role-based access control, and complete employee CRUD operations with real-time frontend-backend integration.

## Features

User Authentication (JWT based login)

Role-Based Access Control (Admin / Staff)

Add Employee

View Employees (Pagination + Filter)

Update Employee

Delete Employee (Soft Delete)

Validation and Error Handling

Loading States and UI Feedback

Deployed Frontend & Backend

## Tech Stack

**Frontend:**
- React
- JavaScript (ES6)
- CSS

**Backend:**
- Python
- Flask
- REST APIs

**Database:**
- SQLite

**Deployment:**
- Vercel (Frontend)
- Render (Backend)

## Architecture Flow

Frontend (React)  
⬇  
API Calls (Fetch / Axios)  
⬇  
Backend (Flask Controllers → Services)  
⬇  
Database (SQLite)


## Live Demo

Frontend: https://python-fullstack-snowy.vercel.app
Backend: https://python-fullstack-q5hz.onrender.com 

##  Authentication Flow

- User logs in with username & password
- Backend validates credentials
- JWT token is generated
- Token is stored in frontend (localStorage)
- Token is sent in Authorization header for protected APIs


## Installation Steps
### Backend:

git clone "https://github.com/jenibaresearcherlyceum-cell/Python_fullstack"
cd project
pip install -r requirements.txt
python app.py
Backend runs at:
  http://127.0.0.1:5000

### Frontend:

cd frontend
npm install
npm run dev
Frontend runs at:
  http://localhost:5173

Screenshots:
Login:
<img width="1920" height="965" alt="image" src="https://github.com/user-attachments/assets/ebfbcbf6-0e3a-47b4-9a66-f7253bdcaf8f" />

Dashboard:
<img width="1920" height="966" alt="image" src="https://github.com/user-attachments/assets/a7fa1022-d7b5-4291-93d6-22c0ccaa4773" />

## Environment Variables

   # Create .env file in frontend:

             VITE_API_URL=http://127.0.0.1:5000

   # For production:

             VITE_API_URL=https://your-render-link.onrender.com

 ## Testing
 
  # Tested APIs using Postman
  # Validated:
        # Authentication
        # CRUD operations
        # Error handling
        # Role-based access
        
  # Fixed issues like:
        # Token errors
        # Data mapping bugs
        # UI loading issues
        
## Future Enhancements
Edit Employee UI
Search and Filter improvements
Role-based UI dashboards
Export data (CSV/Excel)
Performance optimization

## Conclusion

This project demonstrates full stack development skills including API design, authentication, UI development, and deployment.
It reflects real-world application structure and problem-solving ability.

# REST API for AI Chat System using DRF & JWT

**Recruiter Hook:**  
RESTful API for an AI chat system built with Django REST Framework and JWT authentication. Demonstrates secure API development, token‑based auth, and backend design skills relevant to modern web services.

## Overview
This project implements a RESTful backend API for an AI‑powered chat system using **Django REST Framework (DRF)** and **JWT authentication**. The API supports secure user registration and login, token‑based authentication, and endpoints for sending and receiving chat messages powered by a conversational AI.

## Features
- **User Authentication:** Secure registration and login using JWT tokens.  
- **Protected API Endpoints:** Authenticated routes for chat interactions.  
- **AI Chat Interaction:** Backend support for sending messages to an AI service (mock or real) and returning responses.  
- **Extensible Backend:** Easily add new endpoints or integrate with different AI providers.

## Tech Stack
- **Backend Framework:** Python, Django, Django REST Framework  
- **Authentication:** JSON Web Tokens (JWT)  
- **Database:** SQLite (development)  
- **API Tools:** DRF Serializers and ViewSets  
- **Testing:** Postman / API clients (optional)

## How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/elaemmanuel/RestAPI-for-AI-Chat-System-using-DRF-jwt.git
```

2. **Navigate into the project directory**
   

3. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Start the Django server**
```bash
python manage.py runserver
```

6. **Access the API**
- Base API URL: http://127.0.0.1:8000/api/
- Register a user: POST https://127.0.0.1:8000/api/auth/register/
- Login to get JWT tokens: POST https://127.0.0.1:8000/api/auth/login/

7. ## Usage Example
- Register a user using the register endpoint.
- Login to get an access token.
- Use the token to call protected chat endpoints.
- The backend processes and returns AI responses.

## Future Improvements
- Add database entity models for persistent chat history.
- Provide API documentation (Swagger / Redoc).





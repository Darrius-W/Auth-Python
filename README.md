# 🔐 Auth-Python – Token-Based Authentication with FastAPI & React

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.2-blue)](https://reactjs.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Build Status](https://img.shields.io/github/actions/workflow/status/Darrius-W/Auth-Python/python-app.yml?branch=main)](https://github.com/Darrius-W/Auth-Python/actions)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](https://github.com/Darrius-W/Auth-Python/actions)

A full-stack web authentication system built using FastAPI and React, implementing secure JWT-based authentication with HTTP-only cookies, user registration, login, protected routes, and logout functionality.

---

## 🚀 Features

- 🔐 Secure login and registration using JWT tokens (stored in HTTP-only cookies)
- 🔒 Password hashing with bcrypt
- ✅ Protected API routes using FastAPI dependencies
- 🧪 Integration tests with Pytest
- 🎯 Token expiration, logout, and cookie invalidation
- 🌐 CORS configuration for frontend/backend communication

---

## 🛠️ Tech Stack

### Frontend

- React (Hooks, Axios, React Router)
- JavaScript (ES6+)
- HTML5, CSS3

### Backend

- FastAPI
- Python
- Pydantic
- bcrypt, JWT

### Testing

- Pytest (Unit & Integration Tests)

---

## 🔧 Installation & Setup

### 1. Clone the repo

git clone https://github.com/Darrius-W/Auth-Python.git  
cd Auth-Python

### 2. Setup the backend

cd server  
python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  
uvicorn main:app --reload

### 3. Setup the frontend

cd client  
npm install  
npm start

### 4. Run Tests

cd server  
pytest

---

## 🔒 Authentication Flow

1. Signup or Login from React frontend
2. Backend returns JWT token in an HTTP-only cookie
3. Protected routes are accessed only if token is valid
4. `/logout` deletes cookie and ends session

---

## ✅ Example Usage

- Visit `/profile` to see a protected page after logging in
- Manually clear cookies or logout to simulate session expiration

---

## 🧪 Testing Highlights

- ✅ Tested signup, login, protected route access, and logout with Pytest
- ✅ Simulated cookie handling in test client
- ✅ Covers valid and invalid authentication paths

---

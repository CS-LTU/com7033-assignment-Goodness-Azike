# Stroke-Website-Assignment-COM7033

Secure web application for stroke risk prediction and simple patient data management. The system supports authenticated users, a dashboard for key information, and a prediction endpoint powered by a machine learning model.

## Table of contents

- [Overview](#overview)  
- [Key features](#key-features)  
- [System architecture](#system-architecture)  
- [Folder structure](#folder-structure)  
- [Tech stack](#tech-stack)  
- [Getting started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Backend setup](#backend-setup)  
  - [Frontend setup](#frontend-setup)  
- [Environment variables](#environment-variables)  
- [Usage guide](#usage-guide)  
- [Data and model](#data-and-model)  
- [Security and privacy](#security-and-privacy)  
- [Testing](#testing)  
- [Project status and future work](#project-status-and-future-work)  
- [Author and acknowledgements](#author-and-acknowledgements)  

## Overview

Stroke is a leading cause of death and long-term disability. Early risk assessment and clear information for patients support better decisions and treatment planning.

This project delivers an end-to-end web application for stroke risk prediction:

- Collects input from users in a structured form  
- Runs a trained model on the backend  
- Presents predictions via a web interface  
- Stores data in both a relational and a non-relational database to mirror real clinical systems  

The project belongs to the **Secure Software Development** module (COM7033) for the MSc Data Science and Artificial Intelligence programme at Leeds Trinity University.

## Key features

### User authentication and authorisation

- User signup and signin with email and password  
- Passwords hashed before being stored in the database  
- JSON Web Token (JWT) based authentication to protect APIs and pages  

### Stroke data management

- CSV seed scripts (`dataset.csv`, `preprocessed_data.csv`, `seed_data.py`, `init_database.py`) to load and prepare stroke data  
- Separate preprocessing logic in `preprocess.py` and `stroke_data_service.py`  

### Dashboard

- HTML dashboard page with linked JavaScript (`dashboard.html`, `dashboard.js`)  
- Fetches summary data from the backend (for example counts and basic metrics)  
- Uses the same API as the rest of the application  

### Prediction page

- Frontend form for clinical and lifestyle features (`prediction.html`, `prediction.js`)  
- Sends data to a dedicated prediction endpoint in the backend  
- Backend calls the ML model (`model.py`) and returns stroke risk to the UI  

### Security and configuration

- Environment-based configuration using a `.env` file and `python-dotenv`  
- JWT utilities in `jwt_auth.py`  
- Alembic migrations to keep the database schema in sync (where used)  

## System architecture

High-level design.

### Frontend

- Static HTML pages for signup, signin, dashboard and prediction  
- JavaScript files handle form submissions and `fetch` calls to the backend API (`api-config.js`, `script.js`, `dashboard.js`, `prediction.js`)  
- `styles.css` for layout and styling  

### Backend

- FastAPI application started from `server.py`  
- Controller layer in `backend/controller/`:
  - `auth.py` – signup and signin endpoints  
  - `dashboard.py` – endpoints for dashboard data  
  - `prediction.py` – endpoints for stroke prediction  
  - `model.py` – model loading and inference  
  - `preprocess.py` and `stroke_data_service.py` – preprocessing and data utilities  
  - `jwt_auth.py` – JWT token helpers  
- Database connections configured via the `database` package and `mySql_connection.py`  

### Databases

- Relational database (MySQL) for users and stroke-related records, accessed through SQLAlchemy  
- MongoDB planned alongside MySQL for non-relational data and logging (the code handles missing Mongo configuration safely)  

### Machine learning model

- Trained stroke risk model and supporting artefacts stored in the backend  
- Loaded in `model.py` and used by the prediction controller  
- Model performance notes summarised in `model_metrics.txt`  

## Folder structure

```text
com7033-assignment-Goodness-Azike/
├── backend/
│   ├── alembic/
│   │   ├── versions/
│   │   ├── README
│   │   ├── env.py
│   │   └── script.py.mako
│   ├── controller/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── dashboard.py
│   │   ├── jwt_auth.py
│   │   ├── model.py
│   │   ├── prediction.py
│   │   ├── preprocess.py
│   │   └── stroke_data_service.py
│   ├── database/
│   │   ├── mySql_connection.py
│   │   └── mongodb_connection.py
│   ├── tests/
│   │   └── test_password_validation.py
│   ├── .env.example
│   ├── alembic.ini
│   ├── dataset.csv
│   ├── docs.json
│   ├── init_database.py
│   ├── model_metrics.txt
│   ├── preprocessed_data.csv
│   ├── requirements.txt
│   ├── seed_data.py
│   └── server.py
├── frontend/
│   ├── api-config.js
│   ├── dashboard.html
│   ├── dashboard.js
│   ├── index.html
│   ├── prediction.html
│   ├── prediction.js
│   ├── script.js
│   ├── signin.html
│   ├── signup.html
│   ├── styles.css
│   └── .gitignore
├── .gitignore
└── README.md
## Folder Structure (continued)

### Backend
- `server.py` – entry point for the FastAPI web server
- `controller/` – request handlers for auth, dashboard, prediction, preprocessing, data services and JWT
- `database/` – database setup and helpers (MySQL and MongoDB)
- `alembic/` and `alembic.ini` – database migrations (MySQL)
- Data and config files such as `dataset.csv`, `preprocessed_data.csv`, `seed_data.py`, `init_database.py`, `model_metrics.txt`, `docs.json`
- `.env.example` – template for environment variables
- `requirements.txt` – Python dependencies for the backend
- `tests/` – automated tests (for example password validation tests)

### Frontend
- `index.html`, `signin.html`, `signup.html`, `dashboard.html`, `prediction.html` – main pages
- `script.js`, `dashboard.js`, `prediction.js` – page logic and API calls
- `api-config.js` – API base URL and shared settings
- `styles.css` – styling for all pages

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- PyMySQL (MySQL driver)
- Pydantic (request/response models and validation)
- bcrypt (password hashing)
- python-dotenv (environment variable loading)

### Databases
- **MySQL** – main relational database for users and core data
- **MongoDB** – planned for logging and document-style stroke records

### Machine Learning
- Model loaded in Python (e.g. using scikit-learn, as configured in `model.py`)

### Frontend
- HTML, CSS and vanilla JavaScript
- Fetch API for calls to the backend

### Testing
- pytest

*Exact versions are listed in `backend/requirements.txt`.*

## Getting Started

### Prerequisites
- Python 3.9+ installed
- MySQL server available (local instance)
- Optional: MongoDB (local or cloud) for full logging functionality

### Backend Setup

1. Open a terminal and go to the backend folder:
```bash
   cd backend
```

2. Create and activate a virtual environment (example name: senv):
```bash
   python3 -m venv senv
   source senv/bin/activate
```

3. Install Python dependencies:
```bash
   pip install -r requirements.txt
```

4. Create a `.env` file based on `.env.example` (see the next section) and fill in your MySQL credentials and other values.

5. Initialise the database and tables:
```bash
   python3 init_database.py
```

6. Optionally seed data from the CSV:
```bash
   python3 seed_data.py
```

7. Start the backend server:
```bash
   python3 server.py
```
   
   The API runs on http://127.0.0.1:8080.

### Frontend Setup

The frontend is a static HTML/JS site.

1. Open the `frontend` folder in your editor or file browser.

2. For quick local testing, either:
   - Open `index.html` directly in a browser, or
   - Run a simple HTTP server in the frontend folder:
```bash
     cd frontend
     python3 -m http.server 8000
```
     Then visit http://localhost:8000/index.html in your browser.

3. Update `api-config.js` if needed so that the base URL matches your backend (for example `http://127.0.0.1:8080`).

## Environment Variables

The backend uses a `.env` file in the backend folder so that credentials and secrets are not hard coded in the source code.

**Example `.env`:**
```env
dbhost=localhost
dbport=3306
dbuser=root
dbpassword=************
dbname=stroke_db

dburl=mysql+pymysql://root:************@localhost:3306/stroke_db

host=127.0.0.1
port=8080

secret_key=your-long-random-secret-here
expiry_time=1440

mongo_user=
mongo_password=
mongo_cluster=
mongo_name=
```

**Key points:**
- `dbhost`, `dbport`, `dbuser`, `dbpassword`, `dbname` and `dburl` are used to build the MySQL connection.
- `secret_key` is used to sign JWT tokens for authentication.
- `expiry_time` controls how long tokens are valid (in minutes).
- The MongoDB values (`mongo_user`, `mongo_password`, `mongo_cluster`, `mongo_name`) are present for future work but may be left empty on a simple local setup.
- The real `.env` file is ignored by Git via `.gitignore` and is not committed to the repository.

## Usage Guide

### Start the Backend

From the backend folder:
```bash
source senv/bin/activate
python3 server.py
```

The API runs on http://127.0.0.1:8080.

### Open the API Documentation

In a browser, go to: http://127.0.0.1:8080/docs

This opens the FastAPI Swagger UI where you can view and try the API endpoints.

### Create a New User (Signup)

In the `/docs` page:

1. Find `POST /auth/signup` under the authentication section.
2. Click it to expand, then click **Try it out**.
3. Replace the sample JSON with:
```json
   {
     "firstName": "Goodness",
     "lastName": "Azike",
     "email": "goodness@example.com",
     "role": "patient",
     "phone": "07000000000",
     "password": "StrongPass1",
     "confirmPassword": "StrongPass1",
     "dateOfBirth": "1995-01-01",
     "gender": "female"
   }
```
4. Click **Execute**.

A successful response looks like:
```json
{
  "success": true,
  "message": "Account created successfully",
  "data": {
    "name": "Goodness Azike",
    "email": "goodness@example.com"
  }
}
```

### Sign In

Still on `/docs`:

1. Find `POST /auth/signin`.
2. Click **Try it out**.
3. Use:
```json
   {
     "email": "goodness@example.com",
     "password": "StrongPass1"
   }
```
4. Click **Execute**.

A successful response returns a JWT token:
```json
{
  "success": true,
  "message": "Sign in successful",
  "data": {
    "id": 1,
    "name": "Goodness Azike",
    "email": "goodness@example.com",
    "role": "patient",
    "token": "eyJhbGciOiJI..."
  }
}
```

### Use the Token

The value in `data.token` is intended to be sent with requests to protected endpoints using an Authorization header:
```http
Authorization: Bearer eyJhbGciOiJI...
```

In a full deployment, the frontend would attach this token when calling dashboard and prediction APIs.

## Data and Model

- Stroke-related data is stored in `dataset.csv` and `preprocessed_data.csv` in the backend folder.
- Pre-processing (cleaning, encoding, feature handling) is handled in `preprocess.py` and `stroke_data_service.py`.
- The trained machine learning model is loaded in `model.py` and used by the prediction controller.
- Model behaviour and performance are summarised in `model_metrics.txt`.

Further explanation of the dataset, feature engineering and model selection is provided in the COM7033 written report. In this codebase, the focus is on integrating the model securely into a web application.

## Security and Privacy

This project is designed for the Secure Software Development module and applies several secure coding practices:

### Password Hashing
- User passwords are never stored in plain text.
- Passwords are hashed with bcrypt before insertion into the users table.

### Input Validation
- Request bodies are validated using Pydantic models.
- Email addresses use `EmailStr`, which relies on `email-validator`.
- Passwords must meet minimum length and complexity rules (upper case, lower case, digit).

### Authentication and Authorisation
- The `/auth/signin` endpoint issues JSON Web Tokens (JWT).
- Tokens include user id, email, role and an expiry time.
- The JWT secret key and token lifetime are read from environment variables.

### Secure Configuration
- Database credentials and secrets are stored in `.env` and loaded via `python-dotenv`.
- Hard-coded secrets are avoided in the source code.
- The SQLAlchemy connection string is assembled to support special characters in the password.

### Database Design
- The `users` table includes `role`, `phoneNumber`, `DOB` and `gender` to support richer auditing and potential role-based logic.
- Timestamps (`created_at`, `updated_at`) provide a basic audit trail.

### Multi-Database Architecture
- MySQL is the main relational store for authentication and core data.
- MongoDB is planned for logging and storing stroke prediction input/output documents.
- The code is written to fail safely if MongoDB is not configured (the application continues to work with MySQL only).

In the written report, these decisions can be mapped to STRIDE and the OWASP Top Ten.

## Testing

Automated tests are provided using pytest.

From the backend folder:
```bash
source senv/bin/activate
pytest
```

### Current Tests Include:
- A unit test for password validation in the signup model (`tests/test_password_validation.py`), checking that weak passwords are rejected and strong passwords are accepted.

### Manual Testing
Manual testing has been used to exercise the main flows:
- User signup and signin via the FastAPI `/docs` interface.
- Verifying user creation in the MySQL `users` table.
- Observing error handling when invalid credentials or weak passwords are supplied.

Additional tests for the prediction endpoint, data services and MongoDB logging are planned as future work.

## Project Status and Future Work

### Current Status
- Backend API built with FastAPI.
- Secure user signup and signin implemented with hashed passwords and JWT.
- MySQL schema created for users, including role and basic profile fields.
- CSV seeding and data preparation scripts present (`init_database.py`, `seed_data.py`).
- Basic automated tests in place using pytest.
- Project structure and setup documented in this README.

### Planned Improvements
- Complete and enable MongoDB integration for logging stroke prediction events.
- Protect additional endpoints with role-based access control and token checks.
- Extend the dashboard with visualisations of stroke predictions and aggregated statistics.
- Add more detailed logging and monitoring of security-relevant events.
- Increase automated test coverage for controller logic, data access and model integration.
- Package the app for deployment with HTTPS on a cloud platform.

## Author and Acknowledgements

### Author
**Goodness Azike**  
MSc Data Science and Artificial Intelligence  
Leeds Trinity University

### Acknowledgements
- COM7033 Secure Software Development teaching team.
- Open-source libraries used in this project (FastAPI, SQLAlchemy, PyMySQL, bcrypt, Pydantic, python-dotenv, pytest, etc.).
- Public stroke datasets and research that informed model design and evaluation.
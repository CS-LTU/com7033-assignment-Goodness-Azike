# StrokePred – Secure Stroke Risk Prediction Web App

**Module:** COM7033 – Secure Software Development  
**Coursework:** Web Application and Secure Development  
**Student:** Goodness Azike  
**Student ID:** 2409960
**Institution:** Leeds Trinity University

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)

StrokePred is a secure full-stack web application that allows patients to receive a stroke-risk prediction and doctors to review stored predictions in a dashboard. The primary focus of this project is **security, privacy, and responsible use of AI**, rather than building a real medical device. All predictions are for demonstration purposes only.

---

## Table of Contents

- [Overview](#overview)
- [Screenshots](#screenshots)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Folder Structure](#folder-structure)
- [Tech Stack](#tech-stack)
- [Security and Privacy Design](#security-and-privacy-design)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Environment Variables](#environment-variables)
- [Usage Guide](#usage-guide)
- [Machine Learning Model](#machine-learning-model)
- [Doctor Dashboard](#doctor-dashboard)
- [Testing](#testing)
- [Project Status and Future Work](#project-status-and-future-work)
- [AI Assistance and Academic Integrity](#ai-assistance-and-academic-integrity)
- [Author and Acknowledgements](#author-and-acknowledgements)

---

## Overview

Stroke is a leading cause of death and long-term disability. Early risk assessment and clear information for patients support better decisions and treatment planning.

This project delivers an end-to-end web application for stroke risk prediction:

- Collects input from users in a structured form
- Runs a trained machine learning model on the backend
- Presents predictions via a web interface with clear risk levels
- Stores data in both relational (MySQL) and non-relational (MongoDB) databases to mirror real clinical systems

The project belongs to the **Secure Software Development** module (COM7033) for the MSc Data Science and Artificial Intelligence programme at Leeds Trinity University.

---

## Screenshots

### Stroke Risk Assessment Interface
![Stroke Risk Assessment](screenshots/stroke-assessment.png)

The application features:
- **Clean, intuitive form** for entering patient health data
- **Real-time validation** with helpful error messages
- **Clear risk communication** with color-coded results (Low/Moderate/High)
- **Educational disclaimers** emphasizing this is not medical advice
- **Probability scores** to help users understand their risk level

### Additional Views
![Sign In Page](screenshots/signin.png)
*Secure authentication with JWT tokens*

![Doctor Dashboard](screenshots/dashboard.png)
*Doctors can view patient predictions and aggregate statistics*

---

## Key Features

### User Authentication and Authorisation

- User signup and signin with email and password
- Passwords hashed with bcrypt before being stored in the database
- JSON Web Token (JWT) based authentication to protect APIs and pages
- Role-based access control (Patient vs Doctor roles)

### Stroke Data Management

- CSV seed scripts (`dataset.csv`, `preprocessed_data.csv`, `seed_data.py`, `init_database.py`) to load and prepare stroke data
- Separate preprocessing logic in `preprocess.py` and `stroke_data_service.py`

### Patient Prediction Interface

- Frontend form for clinical and lifestyle features (`prediction.html`, `prediction.js`)
- Sends data to a dedicated prediction endpoint in the backend
- Backend calls the ML model (`model.py`) and returns stroke risk to the UI
- Three-tier risk classification: Low, Moderate, High

### Doctor Dashboard

- HTML dashboard page with linked JavaScript (`dashboard.html`, `dashboard.js`)
- Fetches summary data from the backend (total patients, prediction counts, risk breakdowns)
- Paginated table of patient predictions with search functionality
- Modal view for detailed patient information

### Security and Configuration

- Environment-based configuration using a `.env` file and `python-dotenv`
- JWT utilities in `jwt_auth.py`
- Alembic migrations to keep the database schema in sync

---

## System Architecture

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

- **MySQL** – main relational database for users and stroke-related records, accessed through SQLAlchemy
- **MongoDB** – planned alongside MySQL for non-relational data and logging prediction records (the code handles missing Mongo configuration safely)

### Machine Learning Model

- Trained stroke risk model and supporting artifacts stored in the backend
- Loaded in `model.py` and used by the prediction controller
- Model performance notes summarised in `model_metrics.txt`

---

## Folder Structure

```plaintext
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
│   │   ├── test_password_validation.py
│   │   └── test_health_endpoint.py
│   ├── .env.example
│   ├── alembic.ini
│   ├── dataset.csv
│   ├── docs.json
│   ├── init_database.py
│   ├── model_metrics.txt
│   ├── preprocessed_data.csv
│   ├── requirements.txt
│   ├── seed_data.py
│   ├── stroke_model.pkl
│   ├── train_model.py
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
│   └── styles.css
├── screenshots/
│   ├── stroke-assessment.png
│   ├── signin.png
│   └── dashboard.png
├── .gitignore
└── README.md
```

### Backend Components

- `server.py` – entry point for the FastAPI web server
- `controller/` – request handlers for auth, dashboard, prediction, preprocessing, data services and JWT
- `database/` – database setup and helpers (MySQL and MongoDB)
- `alembic/` and `alembic.ini` – database migrations (MySQL)
- Data and config files such as `dataset.csv`, `preprocessed_data.csv`, `seed_data.py`, `init_database.py`, `model_metrics.txt`, `docs.json`
- `.env.example` – template for environment variables
- `requirements.txt` – Python dependencies for the backend
- `tests/` – automated tests (password validation, health endpoint)
- `train_model.py` – script for training the ML model
- `stroke_model.pkl` – serialized trained model

### Frontend Components

- `index.html`, `signin.html`, `signup.html`, `dashboard.html`, `prediction.html` – main pages
- `script.js`, `dashboard.js`, `prediction.js` – page logic and API calls
- `api-config.js` – API base URL and shared settings
- `styles.css` – styling for all pages

---

## Tech Stack

### Backend

- Python 3.9+
- FastAPI
- SQLAlchemy
- PyMySQL (MySQL driver)
- Pydantic (request/response models and validation)
- bcrypt (password hashing)
- python-dotenv (environment variable loading)
- Scikit-learn (machine learning)

### Databases

- **MySQL** – main relational database for users and core data
- **MongoDB** – planned for logging and document-style stroke records

### Machine Learning

- Scikit-learn for model training and inference
- Preprocessing pipeline handles missing values, encoding, and standardization
- Model saved as `stroke_model.pkl`

### Frontend

- HTML, CSS and vanilla JavaScript
- Fetch API for calls to the backend

### Testing

- pytest for automated testing

*Exact versions are listed in `backend/requirements.txt`.*

---

## Security and Privacy Design

This project is designed for the Secure Software Development module and applies several secure coding practices:

### 2.1 Authentication and Authorisation

- JSON Web Tokens (JWT) are issued on successful sign-in
- The client stores a single `user` object (including the token and role) in `localStorage`
- All protected endpoints require a valid `Authorization: Bearer <token>` header, verified in the backend
- Role-based access control:
  - Only users with role `patient` can call `/prediction/predict`
  - Only users with role `doctor` can access `/dashboard/patients` and the doctor dashboard view

### 2.2 Password Handling and Account Security

- User passwords are **never stored in plain text**
- Passwords are hashed with bcrypt before insertion into the users table
- Frontend validation enforces a minimum password policy:
  - At least 8 characters
  - Contains uppercase, lowercase, and numbers
- Backend performs its own validation
- Sign-in and sign-up forms provide clear error messages without leaking sensitive details

### 2.3 Input Validation

- Request bodies are validated using Pydantic models
- Email addresses use `EmailStr`, which relies on `email-validator`
- All form inputs are sanitized and validated on both client and server side

### 2.4 Secure Configuration

- Database credentials and secrets are stored in `.env` and loaded via `python-dotenv`
- Hard-coded secrets are avoided in the source code
- The SQLAlchemy connection string is assembled to support special characters in the password
- JWT secret key and token lifetime are read from environment variables

### 2.5 Database Design

- The `users` table includes `role`, `phoneNumber`, `DOB` and `gender` to support richer auditing and potential role-based logic
- Timestamps (`created_at`, `updated_at`) provide a basic audit trail

### 2.6 Multi-Database Architecture

- MySQL is the main relational store for authentication and core data
- MongoDB is planned for logging and storing stroke prediction input/output documents
- The code is written to fail safely if MongoDB is not configured (the application continues to work with MySQL only)

### 2.7 Data Privacy, UK GDPR and Demo Scope

This is a **local coursework demonstration** and is **not** intended for use by real patients.

- The health information entered on the prediction form is:
  - Sent securely to the backend running on `localhost` on the student's machine
  - Used to generate a stroke-risk prediction with the ML model
  - Optionally stored as a prediction record in a local MongoDB collection (`stroke_data`) for the doctor dashboard
- Data is **not** shared with any third parties and there is no analytics, advertising, or tracking code

The user interface explains:
- How the data is used in this demo
- That this is **not** a substitute for professional medical advice
- That any stored records are only for local coursework evaluation

A **Privacy Policy** link is included in the footer to reflect good practice under **UK GDPR**, even though this system is not deployed publicly.

In a real deployment, additional measures would be required, such as:
- HTTPS/TLS for all traffic
- Encrypted storage and backups
- Formal privacy notice and records of processing
- Data Protection Impact Assessment (DPIA)
- Stronger controls on account lifecycle, logging, and audit trails

In the written report, these decisions can be mapped to STRIDE and the OWASP Top Ten.

---

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

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv senv
   source senv/bin/activate  # On Windows: senv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on `.env.example` and fill in your MySQL credentials and other values (see [Environment Variables](#environment-variables) section).

5. Initialise the database and tables:
   ```bash
   python3 init_database.py
   ```

6. Optionally seed data from the CSV:
   ```bash
   python3 seed_data.py
   ```

7. Train the ML model (if not already trained):
   ```bash
   python3 train_model.py
   ```

8. Start the backend server:
   ```bash
   python3 server.py
   ```
   
   The API runs on http://127.0.0.1:8080

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

---

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

mongo_user=YOUR_MONGO_USER
mongo_password=YOUR_MONGO_PASSWORD
mongo_cluster=YOUR_MONGO_CLUSTER
mongo_name=YOUR_MONGO_DB_NAME
```

**Key points:**

- `dbhost`, `dbport`, `dbuser`, `dbpassword`, `dbname` and `dburl` are used to build the MySQL connection
- `secret_key` is used to sign JWT tokens for authentication
- `expiry_time` controls how long tokens are valid (in minutes)
- The MongoDB values (`mongo_user`, `mongo_password`, `mongo_cluster`, `mongo_name`) are present for future work but may be left empty on a simple local setup
- The real `.env` file is ignored by Git via `.gitignore` and is not committed to the repository

---

## Usage Guide

### Start the Backend

From the backend folder:
```bash
source senv/bin/activate
python3 server.py
```

The API runs on http://127.0.0.1:8080

### Open the API Documentation

In a browser, go to: http://127.0.0.1:8080/docs

This opens the FastAPI Swagger UI where you can view and try the API endpoints.

### Create a New User (Signup)

In the `/docs` page:

1. Find `POST /auth/signup` under the authentication section
2. Click it to expand, then click **Try it out**
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
4. Click **Execute**

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

1. Find `POST /auth/signin`
2. Click **Try it out**
3. Use:
   ```json
   {
     "email": "goodness@example.com",
     "password": "StrongPass1"
   }
   ```
4. Click **Execute**

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

---

## Machine Learning Model

### Training and Preprocessing

The training script `train_model.py` loads the stroke dataset, performs preprocessing and trains a classification model using Scikit-learn.

The preprocessing pipeline (implemented in `preprocess_data`) handles:
- Missing BMI values (imputed or handled as NaN)
- Encoding categorical features (gender, work type, residence type, smoking status)
- Normalization and scaling where appropriate

The trained model is persisted to `stroke_model.pkl` and loaded by the prediction endpoint.

### Prediction Endpoint

The `/prediction/predict` endpoint:

1. Validates the incoming request using Pydantic (`StrokePredictionRequest`)
2. Preprocesses the payload into the correct feature format
3. Calls the model's `predict` and `predict_proba` methods
4. Maps the probability into risk bands:
   - **Low risk** – probability < 0.30
   - **Moderate risk** – 0.30 ≤ probability < 0.60
   - **High risk** – probability ≥ 0.60

5. Returns a structured JSON response with:
   - `prediction` (0 or 1)
   - `probability` (float)
   - `risk_level` (Low / Moderate / High)
   - `message` (user-friendly explanation)

All responses include a disclaimer indicating that this is not a medical diagnosis.

### Model Performance

- Stroke-related data is stored in `dataset.csv` and `preprocessed_data.csv` in the backend folder
- Pre-processing (cleaning, encoding, feature handling) is handled in `preprocess.py` and `stroke_data_service.py`
- Model behaviour and performance are summarised in `model_metrics.txt`

Further explanation of the dataset, feature engineering and model selection is provided in the COM7033 written report. In this codebase, the focus is on integrating the model securely into a web application.

---

## Doctor Dashboard

The doctor dashboard is available at `dashboard.html` for signed-in users with role `doctor`.

### Key Features

**Overview cards with:**
- Total patients
- Total predictions
- Count of Low / Moderate / High-risk predictions

**Paginated table of predictions:**
- Patient name and email
- Age
- Risk level and probability
- Prediction date/time

**Search functionality:**
- Search within the current page by patient name, email, or risk level

**Detail view:**
- "View" button opens a modal showing full details from the stored `input_data`

The backend dashboard endpoint reads from the MongoDB `stroke_data` collection. If MongoDB is not configured, the app still functions for patients, but the dashboard will display "no data".

---

## Testing

Automated tests are provided using pytest.

From the backend folder:

```bash
source senv/bin/activate
pytest
```

### Current Tests Include:

- A unit test for password validation in the signup model (`tests/test_password_validation.py`), checking that weak passwords are rejected and strong passwords are accepted
- A basic health endpoint test (`tests/test_health_endpoint.py`) to verify the API is running

### Manual Testing

Manual testing has been used to exercise the main flows:
- User signup and signin via the FastAPI `/docs` interface
- Verifying user creation in the MySQL `users` table
- Observing error handling when invalid credentials or weak passwords are supplied
- Testing the prediction endpoint with various input combinations
- Verifying role-based access control for patient and doctor endpoints

Additional tests for the prediction endpoint, data services and MongoDB logging are planned as future work.

---

## Project Status and Future Work

### Current Status

- ✅ Backend API built with FastAPI
- ✅ Secure user signup and signin implemented with hashed passwords and JWT
- ✅ MySQL schema created for users, including role and basic profile fields
- ✅ CSV seeding and data preparation scripts present (`init_database.py`, `seed_data.py`)
- ✅ Machine learning model trained and integrated
- ✅ Patient prediction interface with three-tier risk classification
- ✅ Doctor dashboard with statistics and patient records
- ✅ Basic automated tests in place using pytest
- ✅ Project structure and setup documented in this README

### Planned Improvements

- Complete and enable MongoDB integration for logging stroke prediction events
- Protect additional endpoints with role-based access control and token checks
- Extend the dashboard with visualisations of stroke predictions and aggregated statistics
- Add more detailed logging and monitoring of security-relevant events
- Increase automated test coverage for controller logic, data access and model integration
- Implement password reset functionality
- Add email verification for new accounts
- Package the app for deployment with HTTPS on a cloud platform
- Implement rate limiting to prevent abuse
- Add comprehensive API documentation with examples

---

## AI Assistance and Academic Integrity

I used OpenAI ChatGPT (GPT-4) as a coding and writing assistant during this project. Specifically, AI support was used to:

- Refine frontend JavaScript for validation, notifications and usability
- Improve the clarity of comments, documentation and user-facing text
- Debug issues with JWT authentication and role-based access control

**All generated code and text were reviewed, adapted, and tested by me before inclusion.**

I remain responsible for the final design, implementation, and academic integrity of this submission.

---

## Author and Acknowledgements

### Author

**Goodness Azike**  
MSc Data Science and Artificial Intelligence  
Leeds Trinity University  
Student ID: XXXXXXXX

### Acknowledgements

- COM7033 Secure Software Development teaching team
- Open-source libraries used in this project (FastAPI, SQLAlchemy, PyMySQL, bcrypt, Pydantic, python-dotenv, pytest, scikit-learn)
- Public stroke datasets and research that informed model design and evaluation
- The Python and FastAPI communities for excellent documentation and support

---

## License

This project is part of academic coursework for COM7033 at Leeds Trinity University. All rights reserved.

---

**For questions or issues, please contact the author through Leeds Trinity University channels.**
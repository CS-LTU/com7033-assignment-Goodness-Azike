# Stroke-Website-Assignment-COM7033

Secure web application for stroke risk prediction and simple patient data management. The system supports authenticated users, a dashboard for key information, and a prediction page powered by a machine learning model.

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
- Presents predictions on a secure dashboard  
- Stores data in both a relational and a non-relational database to mirror real clinical systems  

The project belongs to the Secure Software Development module (COM7033) for the MSc Data Science and Artificial Intelligence programme at Leeds Trinity University.

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
- Uses the same protected API as the rest of the application  

### Prediction page

- Frontend form for clinical and lifestyle features (`prediction.html`, `prediction.js`)  
- Sends data to a dedicated prediction endpoint in the backend  
- Backend calls the ML model (`model.py`) and returns stroke risk to the UI  

### Security and configuration

- Environment-based configuration using `.env.example`  
- JWT utilities in `jwt_auth.py`  
- Alembic migrations to keep the database schema in sync  

## System architecture

High-level design.

### Frontend

- Static HTML pages for signup, signin, dashboard and prediction  
- JavaScript files handle form submissions and `fetch` calls to the backend API (`api-config.js`, `script.js`, `dashboard.js`, `prediction.js`)  
- `styles.css` for layout and styling  

### Backend

- Python application started from `server.py`  
- Controller layer in `backend/controller/` (`auth.py`, `dashboard.py`, `prediction.py`, `model.py`, `preprocess.py`, `stroke_data_service.py`, `jwt_auth.py`)  
- Database connections and migrations configured via `alembic/`, `alembic.ini` and the `database` package  

### Databases

- Relational database (MySQL) for users and stroke-related records, accessed through the database layer  
- MongoDB used alongside MySQL for non-relational data and logging  

### Machine learning model

- Trained stroke risk model and supporting artefacts stored in the backend  
- Loaded in `model.py` and used by the prediction controller  
- Model performance notes stored in `model_metrics.txt` for reference  

## Folder structure
## Folder structure

```text
Stroke-Website-Project/
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
```


## Backend

- `server.py` – entry point for the web server  
- `controller/` – request handlers for auth, dashboard, prediction, preprocessing, data service and JWT  
- `database/` – database setup and helpers  
- `alembic/` and `alembic.ini` – database migrations  
- Data and config files such as `dataset.csv`, `preprocessed_data.csv`, `seed_data.py`, `init_database.py`, `model_metrics.txt`, `docs.json`  
- `.env.example` – template for environment variables  
- `requirements.txt` – Python dependencies for the backend  

## Frontend

- `index.html`, `signin.html`, `signup.html`, `dashboard.html`, `prediction.html` – main pages  
- `script.js`, `dashboard.js`, `prediction.js` – page logic and API calls  
- `api-config.js` – API base URL and shared settings  
- `styles.css` – styling for all pages  
- `requirements.txt` – notes or extra tools for the frontend  

## Tech stack

- Python  
- Web framework in `server.py` (for example Flask or FastAPI)  
- MySQL as the main relational database  
- Alembic for schema migrations  
- MongoDB for non relational data and logging  
- Machine learning with a Python library such as scikit-learn  
- HTML, CSS and vanilla JavaScript on the frontend  
- JSON Web Tokens (JWT) for authentication  

Update this list with exact versions used in `requirements.txt`.

## Getting started

### Prerequisites

- Python installed  
- MySQL server available  
- MongoDB running locally or in the cloud  

### Backend setup

1. Open a terminal in the `backend` folder.  
2. Create and activate a virtual environment.  
3. Install dependencies with `pip install -r requirements.txt`.  
4. Create a `.env` file from `.env.example` and fill in your values.  
5. Initialise and seed the database using your helper scripts.  
6. Start the backend with `python server.py`.  

### Frontend setup

1. Open the `frontend` folder.  
2. Open `index.html` in a browser, or run a simple local server (for example `python -m http.server 8000`) and go to `http://localhost:8000/index.html`.

## Environment variables

The backend reads configuration from a `.env` file in the `backend` folder.  
Use `.env.example` as a template and create your own `.env` with real values.

Typical variables:

- `SECRET_KEY` – secret key for signing tokens and sessions  
- `MYSQL_URL` – MySQL connection string (host, port, database, user, password)  
- `MONGODB_URI` – MongoDB connection string  
- `ACCESS_TOKEN_EXPIRE_MINUTES` – lifetime of JWT access tokens in minutes  
- `ENV` or `DEBUG` – flag to switch between development and production modes  

Do **not** commit your real `.env` file to Git; it is already ignored by `.gitignore`.

## Usage guide

1. Start the backend in the `backend` folder with `python server.py`.  
2. Open the frontend:
   - either open `index.html` directly in a browser, or  
   - run a local server in the `frontend` folder, for example:

     ```bash
     python -m http.server 8000
     ```

     then go to `http://localhost:8000/index.html`.
3. Go to the **Sign up** page and create a new user account.  
4. Log in via the **Sign in** page.  
5. Open the **Dashboard** to view summary information.  
6. Go to the **Prediction** page.  
7. Enter the clinical and lifestyle details for a test case.  
8. Submit the form and review the stroke risk prediction returned by the model.  

You can repeat steps 6–8 with different inputs to explore the model’s behaviour.

## Data and model

- Stroke-related data is stored in `dataset.csv` and `preprocessed_data.csv`.  
- Pre-processing (cleaning, encoding, feature selection) is handled in `preprocess.py` and related controller logic.  
- The trained machine learning model is loaded in `model.py` and used by the prediction endpoint.  
- Model performance, including metrics such as accuracy, precision, recall and ROC AUC, is summarised in `model_metrics.txt`.  

Further details about the dataset and modelling choices are provided in the COM7033 written report.

## Security and privacy

This project demonstrates secure software development practices:

- Passwords are hashed before being stored in the database (no plain-text storage).  
- Authentication uses **JWT tokens** to protect API endpoints and pages.  
- Sensitive configuration (database URLs, secret keys) is stored in **environment variables**, not hard coded in source files.  
- Input is validated before reaching the database to reduce injection risks.  
- Only authenticated users can access the dashboard and prediction endpoints.  
- Logging is used to record important events such as failed logins and server errors.  

These points can be mapped to STRIDE and the OWASP Top Ten in the accompanying report.

## Testing

Current and planned testing includes:

- Manual testing of key flows (signup, signin, dashboard, prediction).  
- Unit tests for core functions such as preprocessing and model loading.  
- Tests for authentication logic and protected routes.  
- Tests for the prediction endpoint to confirm that valid inputs return a response and invalid inputs are handled safely.  

Once automated tests are added, they can be run with:

```bash
pytest



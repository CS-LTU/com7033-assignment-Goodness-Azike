Stroke-Website-Project

Secure web application for stroke risk prediction and simple patient data management. The system supports authenticated users, a dashboard for key information, and a prediction page powered by a machine learning model.

Table of contents

Overview

Key features

System architecture

Folder structure

Tech stack

Getting started

Prerequisites

Backend setup

Frontend setup

Environment variables

Usage guide

Data and model

Security and privacy

Testing

Project status and future work

Author and acknowledgements

Overview

Stroke remains a leading cause of death and long term disability worldwide. Early risk assessment and clear information for patients support better decisions and treatment planning.

This project delivers a small end to end web application for stroke risk prediction:

Collects input from users in a structured form

Runs a trained model on the backend

Presents predictions on a secure dashboard

Stores data in both a relational and a non-relational database to mirror real clinical systems

The project belongs to the Secure Software Development module (COM7033) for the MSc Data Science and Artificial Intelligence programme at Leeds Trinity University.

Key features

User authentication

Signup and login

Hashed passwords

Session or token based access control

Dashboard

Summary of recent patients or test cases

Overview of recent predictions

Key metrics for the model or system

Prediction page

Form for clinical and lifestyle features

Submission to backend API

Display of predicted stroke risk

Privacy policy page

Short statement on data use

Reference to confidentiality and secure handling of health data

Logging and error handling

Server side logging for key events

Graceful error messages for users

System architecture

High level design:

Frontend

Web interface for patients or clinicians

Communicates with backend over HTTP using JSON

Backend

Python web framework (for example Flask or FastAPI)

REST style API endpoints for authentication, dashboard data, and predictions

Business logic layer separate from routes

Databases

Relational database (for example SQLite or MySQL) for structured data such as users and patient records

MongoDB for additional logging or audit trail data

Machine learning model

Trained stroke risk model stored on disk

Loaded by the backend and used inside prediction endpoints

Folder structure

Example layout.

COM7033-ASSIGNMENT/
├── backend/
│   ├── app.py
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── security/
│   ├── database/
│   └── tests/
├── frontend/
│   ├── public/
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── services/
│       └── styles/
├── requirements.txt
└── README.md


Short description:

backend

app.py, entry point for the web server

routes, API endpoints for auth, dashboard, prediction

services, business logic and helper functions

models, ORM models and the ML model file

security, password hashing, input validation, auth helpers

database, connection settings for SQL and MongoDB

tests, unit and integration tests

frontend

components, reusable UI building blocks

pages, high level screens such as Login, Dashboard, Prediction, Privacy

services, functions for HTTP requests to backend endpoints

styles, CSS or styling framework configuration

Tech stack

Python

Flask or FastAPI (backend web framework)

SQLAlchemy and a relational database such as SQLite or MySQL

MongoDB and a MongoDB driver

A machine learning library such as scikit-learn

Node and npm for frontend tooling

Frontend framework or plain HTML, CSS, JavaScript

Update this list with exact versions used in the project.

Getting started
Prerequisites

Python installed

Node and npm installed

MongoDB running locally or in the cloud

Access to a relational database (for example SQLite file or MySQL server)

Backend setup

Run these steps from the project root.

Clone the repository

Create and activate a virtual environment

Install Python dependencies

pip install -r requirements.txt


Configure environment variables listed in the next section

Run database migrations or create tables if required

Start the backend server

python backend/app.py


Adjust command names to match your files.

Frontend setup

Move into the frontend folder

cd frontend


Install dependencies

npm install


Start the development server

npm start


Open the shown address in a browser, usually http://localhost:3000

Environment variables

Configure sensitive settings through environment variables rather than hard coding them.

Example list:

SECRET_KEY
Secret key for the web framework.

SQLALCHEMY_DATABASE_URI
Connection string for the relational database.

MONGODB_URI
Connection string for MongoDB.

ACCESS_TOKEN_EXPIRE_MINUTES
Lifetime for login tokens.

DEBUG
Flag for development or production mode.

Explain where to store these variables, for example in a .env file that remains out of version control.

Usage guide

Visit the frontend address in a browser.

Create a new user account or use demo credentials provided by the lecturer.

Sign in.

Explore the dashboard.

Open the prediction page.

Enter patient or test data in the form.

Submit the form and view the output stroke risk label or probability.

Include screenshots later to illustrate the flow.

Data and model

Dataset source, for example a public stroke dataset from Kaggle or another repository.

Features used, such as age, gender, hypertension, heart disease, body mass index, smoking status.

Model type, for example logistic regression, random forest, or gradient boosting.

Preprocessing steps, such as encoding, scaling, and handling of missing values.

Basic performance metrics, such as accuracy, precision, recall, F1 score, ROC AUC.

Mention any checks on bias or fairness, for example performance across groups.

Security and privacy

Points covered for the Secure Software Development module:

Password hashing with a strong algorithm such as bcrypt or Argon2

Input validation and output encoding to limit injection attacks

Protection against common OWASP issues such as SQL injection, cross site scripting, weak authentication, and insecure direct object references

Role based access control for pages with sensitive information

Secure handling of environment variables and secrets

Logging of security relevant events such as failed logins

Highlight links to STRIDE or OWASP Top Ten items where relevant.

Testing

Unit tests for core functions and services

Tests for authentication and authorisation logic

Tests for prediction endpoints

Optional simple load or stress tests

Show command for running the test suite, for example:

pytest

Project status and future work

Current status:

Core features implemented

Basic model integrated with the backend

Frontend linked to API routes

Planned improvements:

Richer visualisation on the dashboard

Better explanation of model predictions

More extensive logging and monitoring

Deployment to a cloud platform with HTTPS

Update this section during development.

Author and acknowledgements

Author

Goodness Azike

MSc Data Science and Artificial Intelligence

Leeds Trinity University

Acknowledgements

COM7033 Secure Software Development teaching team

Open source libraries and datasets used in the project
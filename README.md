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
│   ├── README.md
│   ├── api-config.js
│   ├── dashboard.html
│   ├── dashboard.js
│   ├── index.html
│   ├── prediction.html
│   ├── prediction.js
│   ├── requirements.txt
│   ├── script.js
│   ├── signin.html
│   ├── signup.html
│   ├── styles.css
│   └── .gitignore
├── .gitignore
└── README.md

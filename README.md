# Stroke-Website-Project

Secure web application for stroke risk prediction and simple patient data management. The system supports authenticated users, a dashboard for key information, and a prediction page powered by a machine learning model.

## Table of contents

- Overview  
- Key features  
- System architecture  
- Folder structure  
- Tech stack  
- Getting started  
  - Prerequisites  
  - Backend setup  
  - Frontend setup  
- Environment variables  
- Usage guide  
- Data and model  
- Security and privacy  
- Testing  
- Project status and future work  
- Author and acknowledgements  

## Overview

Stroke is a leading cause of death and long term disability. Early risk assessment and clear information for patients support better decisions and treatment planning.

This project delivers a small end to end web application for stroke risk prediction:

- Collects input from users in a structured form  
- Runs a trained model on the backend  
- Presents predictions on a secure dashboard  
- Stores data in both a relational and a non-relational database to mirror real clinical systems  

The project belongs to the Secure Software Development module (COM7033) for the MSc Data Science and Artificial Intelligence programme at Leeds Trinity University.

## Key features

- **User authentication**  
  - Signup and login  
  - Hashed passwords  
  - Token or session based access control  

- **Dashboard**  
  - Summary of recent patients or test cases  
  - Overview of recent predictions  
  - Key metrics for the model or system  

- **Prediction page**  
  - Form for clinical and lifestyle features  
  - Submission to backend API  
  - Display of predicted stroke risk  

- **Privacy policy page**  
  - Short statement on data use  
  - Reference to confidentiality and secure handling of health data  

- **Logging and error handling**  
  - Server side logging for key events  
  - Graceful error messages for users  

## System architecture

High level design:

- **Frontend**  
  - Web interface for patients or clinicians  
  - Communicates with backend over HTTP using JSON  

- **Backend**  
  - Python web framework (for example Flask or FastAPI)  
  - REST style API endpoints for authentication, dashboard data, and predictions  
  - Business logic layer separate from routes  

- **Databases**  
  - Relational database (for example SQLite or MySQL) for structured data such as users and patient records  
  - MongoDB for additional logging or audit trail data  

- **Machine learning model**  
  - Trained stroke risk model stored on disk  
  - Loaded by the backend and used inside prediction endpoints  

## Folder structure

```text
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

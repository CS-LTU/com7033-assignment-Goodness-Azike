import pandas as pd
import sys
import os
import bcrypt
from datetime import datetime
from sqlalchemy import text

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database.mySql_connection import db
from database.mongodb_connection import stroke_collection

def create_user(gender, age, row_id):
    """Create a user in MySQL and return the user ID"""
    try:
        email = f"patient_{row_id}@strokeapp.com"
        name = f"Patient {row_id}"
        
        default_password = "Patient123!"
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(default_password.encode('utf-8'), salt).decode('utf-8')
        
        gender_str = str(gender).strip().lower()
        gender_mapped = gender_str if gender_str in ['male', 'female'] else 'male'
        
        current_year = datetime.now().year
        birth_year = current_year - int(age)
        dob = f"{birth_year}-01-01"
        
        check_user_query = text("SELECT id FROM users WHERE email = :email")
        existing_user = db.execute(check_user_query, {'email': email}).fetchone()
        
        if existing_user:
            return existing_user.id
        
        insert_user_query = text("""
            INSERT INTO users (name, email, password, role, phoneNumber, DOB, gender)
            VALUES (:name, :email, :password, :role, :phoneNumber, :DOB, :gender)
        """)
        
        result = db.execute(insert_user_query, {
            'name': name,
            'email': email,
            'password': hashed_password,
            'role': 'patient',
            'phoneNumber': None,
            'DOB': dob,
            'gender': gender_mapped
        })
        db.commit()
        
        get_user_query = text("SELECT id FROM users WHERE email = :email")
        user = db.execute(get_user_query, {'email': email}).fetchone()
        
        return user.id
    
    except Exception as e:
        db.rollback()
        print(f"Error creating user for row {row_id}: {e}")
        return None




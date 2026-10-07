import csv
import sqlite3
import io

import joblib
import numpy as np
import pandas as pd
import xgboost as xgb

from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
import mysql.connector
from mysql.connector import Error
import hashlib

#from tensorflow.python.keras.models import model_from_json

app = Flask(__name__)
"""
try:
    with open("model.json", "r") as json_file:
        loaded_model_json = json_file.read()
    model = model_from_json(loaded_model_json)
    model.load_weights("model_weights.h5")  # Ensure weights file exists
except Exception as e:
    raise ValueError(f"Error loading model: {e}")

try:
    label_encoder = joblib.load("label_encoder.pkl")
except Exception as e:
    raise ValueError(f"Error loading label encoder: {e}")
"""

# Configuration de la connexion à la base de données
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',  # Assurez-vous que le serveur MySQL est en cours d'exécution localement
        database='db1',  # Remplacez par le nom de votre base de données
        user='root',  # Remplacez par votre nom d'utilisateur MySQL
        password=''  # Remplacez par votre mot de passe MySQL
    )



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Hacher le mot de passe
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)

            # Vérifier si l'utilisateur existe dans la base de données
            cursor.execute(
                "SELECT * FROM Users WHERE email = %s AND password_hash = %s",
                (email, hashed_password)
            )
            user = cursor.fetchone()
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

        if user:
            return redirect(url_for('maladie'))
        else:
            return "Nom d'utilisateur, email ou mot de passe incorrect"

    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        speciality = request.form['speciality']
        nom = request.form['nom']

        # Hacher le mot de passe
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            # Vérifier si l'utilisateur existe déjà
            cursor.execute("SELECT * FROM Users WHERE email = %s", (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                return "L'utilisateur ou l'email existe déjà, veuillez en choisir un autre."

            # Insérer le nouvel utilisateur dans la base de données
            cursor.execute(
                "INSERT INTO Users (email, password_hash, speciality, nom) VALUES (%s, %s, %s, %s)",
                (email, hashed_password, speciality, nom)
            )
            connection.commit()
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

        return redirect(url_for('login'))

    return render_template('register.html')


    



    # Afficher le formulaire si méthode GET
    return render_template('module1/templates/symptom.html')



@app.route('/maladie')
def maladie():
    return render_template('maladie.html')











if __name__ == '__main__':
    app.run(debug=True)


















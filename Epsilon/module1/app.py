import csv
import io
from urllib import request

import mysql
from flask import Flask, send_file


app = Flask(__name__)
# Configuration de la connexion à la base de données
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',  # Assurez-vous que le serveur MySQL est en cours d'exécution localement
        database='db1',  # Remplacez par le nom de votre base de données
        user='root',  # Remplacez par votre nom d'utilisateur MySQL
        password=''  # Remplacez par votre mot de passe MySQL
    )

@app.route('/')
def index():
    return send_file('symptom.html')

@app.route("/predict", methods=["POST"])
def predict():
    e1 = request.form.get("att1")
    e2 = request.form.get("att2")
    e3 = request.form.get("att3")
    e4 = request.form.get("att4")
    e5 = request.form.get("att5")
    blood_test_results = {
        "Glucose": request.form.get("att1"),
        "Cholesterol":request.form.get("att2") ,
        "White Blood Cells (WBC)":request.form.get("att3"),
        "Red Blood Cells (RBC)": request.form.get("att4"),
        "Mean Corpuscular Volume (MCV)": request.form.get("att5")
    }
    """# Predict
    sample_data = np.array([[e1, e2, e3, e4, e5]])
    sample_prediction = model.predict(sample_data)
    sample_prediction_decoded = label_encoder.inverse_transform([np.argmax(sample_prediction)])
    prediction = sample_prediction_decoded[0]"""

@app.route('/export', methods=['GET'])
def export_data():
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch all patient data
    query = """
        SELECT `COL 1`, `COL 2`, `COL 3`, `COL 4`, `COL 5`,`COL 6`
        FROM blood_samples_selected_columns_1_
    """
    """cursor.execute(query)
    rows = cursor.fetchall()

    # Generate CSV
    output = io.StringIO()  # Use StringIO for string-based CSV writing
    writer = csv.writer(output)
    writer.writerow(['COL 1', 'COL 2', 'COL 3', 'COL 4', 'COL 5','COL 6'])  # Header
    writer.writerows(rows)
    output.seek(0)

    # Convert StringIO content to BytesIO for Flask's `send_file`
    memory_file = io.BytesIO(output.getvalue().encode('utf-8'))
    output.close()

    # Close DB connection
    cursor.close()
    conn.close()

    # Send CSV as a downloadable file
    return send_file(
        memory_file,
        mimetype='text/csv',
        as_attachment=True,
        download_name='patient_data.csv'
    )"""

if __name__ == '__main__':
    app.run(debug=True)
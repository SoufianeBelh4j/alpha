import mysql
from flask import Flask, render_template

app = Flask(__name__)



def get_db_connection():
    return mysql.connector.connect(
        host='localhost',  # Assurez-vous que le serveur MySQL est en cours d'exécution localement
        database='db1',  # Remplacez par le nom de votre base de données
        user='root',  # Remplacez par votre nom d'utilisateur MySQL
        password=''  # Remplacez par votre mot de passe MySQL
    )

@app.route("/", methods=["POST","GET"])
def symb():
    return render_template('beta.html')

@app.route("/psymb", methods=["POST","GET"])
def psymb():
    return render_template("bpredict.html")

if __name__ == '__main__':
    app.run(debug=True)
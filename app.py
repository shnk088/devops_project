from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        db = mysql.connector.connect(
            host="db",
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        return "Flask + MySQL connected successfully 🚀"
    except Exception as e:
        return f"Database connection failed ❌ : {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

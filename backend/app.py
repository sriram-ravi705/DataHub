from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Fetch database connection details from environment variables
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USERNAME = os.getenv('MYSQL_USERNAME')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

# Connect to MySQL Database (Function to be used later)
def get_db_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USERNAME,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

@app.route('/')
def index():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM test_table;")  # Fetch all rows from the test_table
        result = cursor.fetchall()  # Use fetchall() to get all rows
        cursor.close()
        connection.close()
        return jsonify(result)  # Return all records as JSON
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/add', methods=['POST'])
def add_record():
    try:
        # Get the data sent from the frontend
        data = request.get_json()
        name = data['name']  # Retrieve 'name' from the request body

        # Insert the data into the MySQL database
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO test_table (name) VALUES (%s)", (name,))
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({'message': 'Data added successfully', 'name': name}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database connection function
def get_db_connection():
    return psycopg2.connect(
        dbname="ticket_system",
        user="postgres",
        password="123",  # Replace with your PostgreSQL password
        host="localhost",
        port="5432"
    )

# API to create a new ticket
@app.route('/tickets', methods=['POST', 'GET'])
def tickets():
    if request.method == 'GET':
        return jsonify({"message": "This endpoint is for creating tickets. Use POST with the required data."})

    try:
        # Get JSON data from request
        data = request.get_json()
        customer_name = data.get('customer_name')
        issue_description = data.get('issue_description')
        urgency = data.get('urgency')
        department = data.get('department')

        # Validate input
        if not customer_name or not issue_description or not urgency or not department:
            return jsonify({"error": "All fields are required"}), 400

        # Determine the table based on urgency
        table_name = None
        if urgency.lower() == "low":
            table_name = "low_urgency"
        elif urgency.lower() == "medium":
            table_name = "medium_urgency"
        elif urgency.lower() == "high":
            table_name = "high_urgency"
        else:
            return jsonify({"error": "Invalid urgency level"}), 400

        # Insert data into the respective table
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        query = f"""
            INSERT INTO {table_name} (customer_name, issue_description, department) 
            VALUES (%s, %s, %s) RETURNING ticket_id;
        """
        cursor.execute(query, (customer_name, issue_description, department))
        ticket_id = cursor.fetchone()['ticket_id']
        conn.commit()

        return jsonify({"id": ticket_id}), 201

    except psycopg2.Error as db_error:
        return jsonify({"error": f"Database error: {db_error}"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        # Ensure the connection is closed
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == "__main__":
    app.run(debug=True)

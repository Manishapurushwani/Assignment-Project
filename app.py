from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import mysql.connector

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")  # Adjust CORS policy as needed

# Database connection details
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="merababa1",
    database="dishes"
)

# Function to fetch all dishes from the database
def fetch_dishes():
    cursor = db_connection.cursor(dictionary=True)
    query = "SELECT * FROM dishes"
    cursor.execute(query)
    dishes = cursor.fetchall()
    cursor.close()
    return dishes

# Function to toggle the isPublished status of a dish
def toggle_published_status(dish_id):
    cursor = db_connection.cursor()
    # Fetch current isPublished status
    cursor.execute("SELECT isPublished FROM dishes WHERE dishId = %s", (dish_id,))
    current_status = cursor.fetchone()[0]
    # Toggle status
    new_status = not current_status
    # Update database
    cursor.execute("UPDATE dishes SET isPublished = %s WHERE dishId = %s", (new_status, dish_id))
    db_connection.commit()
    cursor.close()
    return new_status

# API endpoint to fetch all dishes
@app.route('/api/dishes', methods=['GET'])
def get_dishes():
    dishes = fetch_dishes()
    return jsonify(dishes)

# API endpoint to toggle isPublished status of a dish
@app.route('/api/dishes/<int:dish_id>/publish', methods=['PUT'])
def toggle_publish_dish(dish_id):
    new_status = toggle_published_status(dish_id)
    # Emit event to notify clients about the change
    socketio.emit('dishStatusChanged', {'dishId': dish_id, 'isPublished': new_status}, broadcast=True)
    return jsonify({"dishId": dish_id, "isPublished": new_status})

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)

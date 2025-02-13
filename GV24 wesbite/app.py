from flask import Flask, render_template, jsonify, request
import random
import time
import psycopg2

app = Flask(__name__)

# parameters to connect to TimescaleDB
conn_params = {
    'dbname': 'gridville',
    'user': 'postgres', 
    'password': 'postgres', 
    'host': 'localhost',  #localhost as its local idk
    'port': 5432  # default PostgreSQL port
}

# Establish a connection to the database
try:
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()
    conn.commit()
    print("database connected")

except Exception as e:
    print(f"Database connection error: {e}")


# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index1.html')

# Route to serve the new HTML page
@app.route('/time_range')
def time_range():
    return render_template('time_range1.html')

# Existing endpoint to fetch data for a selected time range
@app.route('/fetch_data_range')
def fetch_data_range():
    from_time = request.args.get('from')
    to_time = request.args.get('to')

    try:
        # Fetch data from the sensors table within the given time range
        cursor.execute("SELECT * FROM sensor_data2 WHERE time >= %s AND time <= %s ORDER BY time ASC;", (from_time, to_time))
        records = cursor.fetchall()

        # Prepare data to return as JSON
        data = []
        for record in records:
            data.append({
                'time': record[0],  # Assuming the first column is time
                'sensor_1': record[1],
                'sensor_2': record[2],
                'sensor_3': record[3],
                'sensor_4': record[4],
                'sensor_5': record[5],
                'sensor_6': record[6],
                'sensor_7': record[7],
                'sensor_8': record[8],
                'sensor_9': record[9],
                'sensor_10': record[10]
            })

        return jsonify(data)  # Return data as JSON response

    except Exception as e:
        print(f"Failed to fetch data: {e}")
        return jsonify({"error": "Failed to fetch data"}), 500
    
# Endpoint to send random data for testing (mimicking sensor data)
@app.route('/fetch_data')
def fetch_data():
    try:
        # Fetch data from the sensors table
        cursor.execute("SELECT * FROM sensor_data2 ORDER BY time DESC LIMIT 2;")
        records = cursor.fetchall()

        # Prepare data to return as JSON
        data = []
        for record in records:
            data.append({
                'time': record[0],  # Assuming the first column is time
                'sensor_1': record[1],
                'sensor_2': record[2],
                'sensor_3': record[3],
                'sensor_4': record[4],
                'sensor_5': record[5],
                'sensor_6': record[6],
                'sensor_7': record[7],
                'sensor_8': record[8],
                'sensor_9': record[9],
                'sensor_10': record[10]
            })
            

        return jsonify(data)  # Return data as JSON response

    except Exception as e:
        print(f"Failed to fetch data: {e}")
        return jsonify({"error": "Failed to fetch data"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# Close the db connection when the app is stopped
@app.teardown_appcontext
def close_connection(exception):
    # This function can be kept empty if using connection per request
    pass
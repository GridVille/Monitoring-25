import random
import time
import psycopg2

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

#generate fake data to 
iteration = 0
def genData():

    global iteration
    #fake data genereation
    sensor_data = {
        'sensor_1': round(random.uniform(5, 15), 2),
        'sensor_2': round(random.uniform(12, 20), 2),
        'sensor_3': round(random.uniform(10, 54), 2),
        'sensor_4': round(random.uniform(40, 54), 2),
        'sensor_5': round(random.uniform(10, 20), 2),
        'sensor_6': round(random.uniform(12, 18), 2),
        'sensor_7': round(random.uniform(10, 15), 2),
        'sensor_8': round(random.uniform(10, 20), 2),
        'sensor_9': round(random.uniform(12, 30), 2),
        'sensor_10': round(random.uniform(10, 24), 2)
    }

    # Insert data into TimescaleDB sensor_data
    try:
        cursor.execute("""
        INSERT INTO sensor_data2 (
            time, sensor_1, sensor_2, sensor_3, sensor_4, sensor_5,
            sensor_6, sensor_7, sensor_8, sensor_9, sensor_10
        )
        VALUES (NOW(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, tuple(sensor_data.values()))
        conn.commit()

        #signal data sent
        print("data sent to DB", iteration)
        iteration += 1

    except Exception as e:
        print(f"Failed to insert data: {e}")

# close the db connection when app is stopped
def close_connection(exception):
    if conn:
        cursor.close()
        conn.close()

while(True):
    genData()
    time.sleep(1)
import mysql.connector

# Database configuration
db_config = {
    'user': 'hbnb_dev',
    'password': 'hbnb_dev_pwd',
    'host': 'localhost',
    'database': 'hbnb_dev_db'
}

# Connect to the database
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Example: Inserting data into states table
    insert_query = "INSERT INTO states (name) VALUES (%s)"
    state_name = ('California',)
    cursor.execute(insert_query, state_name)

    # Commit the changes
    connection.commit()
    print("Data inserted successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()


import mysql.connector
from mysql.connector import Error

class DBStorage:
    def __init__(self, user, password, host, database):
        self.connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_state(self, name):
        query = "INSERT INTO states (name) VALUES (%s)"
        self.cursor.execute(query, (name,))
        self.connection.commit()
        return self.cursor.lastrowid

    def create_city(self, state_id, name):
        query = "INSERT INTO cities (state_id, name) VALUES (%s, %s)"
        self.cursor.execute(query, (state_id, name))
        self.connection.commit()
        return self.cursor.lastrowid

    def create_user(self, email, password, first_name, last_name):
        query = "INSERT INTO users (email, password, first_name, last_name) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (email, password, first_name, last_name))
        self.connection.commit()
        return self.cursor.lastrowid

    def create_place(self, city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude):
        query = """INSERT INTO places (city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        self.cursor.execute(query, (city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude))
        self.connection.commit()
        return self.cursor.lastrowid

    def place_exists(self, place_id):
        query = "SELECT * FROM places WHERE id = %s"
        self.cursor.execute(query, (place_id,))
        return self.cursor.fetchone() is not None

    def close(self):
        self.cursor.close()
        self.connection.close()

if __name__ == "__main__":
    # Database connection parameters
    db = DBStorage(user='your_username', password='your_password', host='localhost', database='hbnb_dev_db')
    
    # Create State
    state_id = db.create_state("California")
    print(f"Test create State name='California' with ID: {state_id}")

    # Create City
    city_id = db.create_city(state_id, "San_Francisco_is_super_cool")
    print(f"Create City state_id='{state_id}' name='San_Francisco_is_super_cool' with ID: {city_id}")

    # Create User
    user_id = db.create_user("my@me.com", "pwd", "FN", "LN")
    print(f"Create User email='my@me.com' password='pwd' first_name='FN' last_name='LN' with ID: {user_id}")

    # Create Place
    place_id = db.create_place(
        city_id=city_id, 
        user_id=user_id, 
        name="My_house", 
        description="no_description_yet", 
        number_rooms=4, 
        number_bathrooms=1, 
        max_guest=3, 
        price_by_night=100.00, 
        latitude=120.12, 
        longitude=101.4
    )
    print(f"Create Place city_id='{city_id}' user_id='{user_id}' name='My_house' with ID: {place_id}")

    # Verify Place Exists
    if db.place_exists(place_id):
        print(f"Show Place {place_id} is present (integer + float).")
    else:
        print(f"Place {place_id} is NOT present in the database.")

    # Close the database connection
    db.close()


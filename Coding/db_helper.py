# db_helper.py

import mysql.connector

# Global connection object
global cnx

# Establish the database connection
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SQL@123",
    database="pandeyji_eatery"
)

# Function to fetch the order status from the order_tracking table
def get_order_status(order_id: int):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = f"SELECT status FROM order_tracking WHERE order_id = {order_id}"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # Returning the order status
    if result:
        return result[0]
    else:
        return None

# Function to add an order item to the database
def add_order_to_db(food_item: str, quantity: int, order_id: int):
    cursor = cnx.cursor()
    args = (food_item, quantity, order_id)
    cursor.callproc('insert_order_item', args)
    cnx.commit()
    cursor.close()

# Function to get the new order ID
def get_new_order_id():
    cursor = cnx.cursor()
    cursor.execute('SELECT DISTINCT MAX(order_id) FROM orders')
    result = cursor.fetchone()[0]
    cursor.close()
    return result + 1

# Function to add an order tracking entry to the database
def add_order_track_to_db(order_id: int):
    cursor = cnx.cursor()
    cursor.execute(f"INSERT INTO order_tracking VALUES({order_id},'In progress')")
    cnx.commit()
    cursor.close()

# Function to get the total price of an order
def get_total(order_id: int):
    cursor = cnx.cursor()
    cursor.execute(f'SELECT SUM(total_price) FROM orders WHERE order_id={order_id}')
    result = cursor.fetchone()[0]
    cursor.close()
    return result

#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust user/password/host as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # Change to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Attempt to create the database (won't fail if it exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close cursor and connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    create_database()

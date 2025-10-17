import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (change credentials if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Add your MySQL root password if you set one
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Use CREATE DATABASE IF NOT EXISTS to avoid failure if it already exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL or creating database: {e}")

    finally:
        # Always close cursor and connection if they exist
        try:
            if cursor:
                cursor.close()
            if connection.is_connected():
                connection.close()
        except:
            pass

if __name__ == "__main__":
    create_database()

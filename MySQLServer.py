
"""
MySQLServer.py
Script to create the database 'alx_book_store' in MySQL.
"""

import mysql.connector
from mysql.connector import Error

def main():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        try:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
        except NameError:
            pass

if __name__ == "__main__":
    main()

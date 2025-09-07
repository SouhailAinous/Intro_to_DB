#!/usr/bin/env python3
"""
MySQLServer.py
Script to create the database 'alx_book_store' in MySQL.
"""

import mysql.connector

def main():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if cursor is not None:
            try:
                cursor.close()
            except mysql.connector.Error:
                pass
        if connection is not None and connection.is_connected():
            try:
                connection.close()
            except mysql.connector.Error:
                pass

if __name__ == "__main__":
    main()

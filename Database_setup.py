import mysql.connector

# Establish connection to MySQL without specifying database initially
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="merababa1"
)

# Create cursor object to execute queries
cursor = db_connection.cursor()

# SQL statement to create 'dishes' database if it doesn't exist
create_database_query = "CREATE DATABASE IF NOT EXISTS dishes"

# Execute the create database query
cursor.execute(create_database_query)

# Switch to 'dishes' database
cursor.execute("USE dishes")

# SQL statement to create dishes table
create_table_query = """
CREATE TABLE IF NOT EXISTS dishes (
    dishId INT AUTO_INCREMENT PRIMARY KEY,
    dishName VARCHAR(255) NOT NULL,
    imageUrl VARCHAR(255) NOT NULL,
    isPublished BOOLEAN NOT NULL
)
"""

# Execute the create table query
cursor.execute(create_table_query)

# Sample data to insert into the dishes table
dishes_data = [
    {
        "dishName": "Jeera Rice",
        "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/jeera-rice.jpg",
        "isPublished": True
    },
    {
        "dishName": "Paneer Tikka",
        "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/paneer-tikka.jpg",
        "isPublished": True
    },
    {
        "dishName": "Rabdi",
        "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/rabdi.jpg",
        "isPublished": True
    },
    {
        "dishName": "Chicken Biryani",
        "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/chicken-biryani.jpg",
        "isPublished": True
    },
    {
        "dishName": "Alfredo Pasta",
        "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/alfredo-pasta.jpg",
        "isPublished": True
    }
]

# SQL statement to insert data into dishes table
insert_query = """
INSERT INTO dishes (dishName, imageUrl, isPublished)
VALUES (%s, %s, %s)
"""

# Insert each dish data into the dishes table
for dish in dishes_data:
    dish_values = (dish["dishName"], dish["imageUrl"], dish["isPublished"])
    cursor.execute(insert_query, dish_values)

# Commit changes to the database
db_connection.commit()

# Close cursor and connection
cursor.close()
db_connection.close()

print("Database 'dishes' and table 'dishes' created successfully, and data inserted into 'dishes' table.")

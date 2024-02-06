import sqlite3

def get_unique_paths(database_path):
    # Connect to the SQLite database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Execute the SQL query to select unique paths
    query = "SELECT DISTINCT Path FROM All_Images"
    cursor.execute(query)

    # Fetch all the unique paths as a list
    unique_paths = [row[0] for row in cursor.fetchall()]

    # Close the database connection
    connection.close()

    return unique_paths

# Replace 'All_Images.db' with the actual path to your database file
database_path = 'All_Images.db'
unique_paths_list = get_unique_paths(database_path)

# Print or use the unique paths list as needed
print(unique_paths_list)
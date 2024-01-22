
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


cluster_name = "cluster0"
username = "sebastianheckner1995"
password = "jQpPmqIEHV6PPhim"
uri = "mongodb+srv://sebastianheckner1995:jQpPmqIEHV6PPhim@cluster0.ej5xn85.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# create database
database = client['imedup']


    # This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    # Get the database
    print(database)
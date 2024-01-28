
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
# create collection
collection = database.test_collection
# example entry
example_entry = {'id': 1,
                'pipeline_param': 4,
                'image_hex': 0x62AF87}
# insert example into database and get its id
post_id = collection.insert_one(example_entry).inserted_id
# find a certain entry in the database, based on its id that we gave it
result = collection.find_one({'id': 1})


if __name__ == "__main__":
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    # tests
    print(database)
    print(collection)
    print(database.list_collection_names())
    print(result)
    print(post_id)
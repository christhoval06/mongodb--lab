from pymongo import MongoClient


def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    #    CONNECTION_STRING = "mongodb+srv://root:admin@mongodb/films"
    CONNECTION_STRING = "mongodb://root:admin@mongodb:27017/"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    # client = MongoClient(
    #     host = [ str('mongodb') + ":" + str('27017') ],
    #     serverSelectionTimeoutMS = 3000, # 3 second timeout
    #     username = "root",
    #     password = "admin",
    # )

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['films']

# # This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":

#    # Get the database
#    dbname = get_database()

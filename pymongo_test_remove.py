# Get the database using the method we defined in pymongo_test_insert file
from bson.objectid import ObjectId
from dateutil import parser

from pymongo_get_database import get_database

dbname = get_database()

collection_name = dbname["foods"]


filter = {"item_name" : "Tomato Sauce"}

res = collection_name.delete_one(filter) 

print(res)


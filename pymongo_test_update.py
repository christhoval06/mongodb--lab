# Get the database using the method we defined in pymongo_test_insert file
from bson.objectid import ObjectId
from dateutil import parser

from pymongo_get_database import get_database

dbname = get_database()

collection_name = dbname["foods"]


expiry_date = '2025-07-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)
tomato_sauce = collection_name.insert_one({
  "item_name" : "Tomato Sauce",
  "quantity" : 1,
  "ingredients" : ObjectId('663638412b0ac9e69001a377'),
  "expiry_date" : expiry
})

filter = {"item_name" : "Tomato Sauce"}
newvalues = { "$set": { 'quantity': 25, "use": 'cooking' } }

tomato_sauce = collection_name.update_one(filter, newvalues) 

print(tomato_sauce)


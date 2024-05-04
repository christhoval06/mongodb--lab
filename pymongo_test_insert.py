# Get the database using the method we defined in pymongo_test_insert file
from dateutil import parser

from pymongo_get_database import get_database

dbname = get_database('films')

collection_name = dbname["foods"]


expiry_date = '2021-07-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)
item_3 = {
  "item_name" : "Bread",
  "quantity" : 2,
  "ingredients" : "all-purpose flour",
  "expiry_date" : expiry
}
collection_name.insert_one(item_3)
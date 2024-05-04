# Get the database using the method we defined in pymongo_test_insert file
from pandas import DataFrame
from pymongo_get_database import get_database

dbname = get_database()
 
# Retrieve a collection named "foods" from database
collection_name = dbname["foods"]
 
item_details = collection_name.find()
# item_details = collection_name.find({"genres" : "Romance"})
# convert the dictionary objects to dataframe
items_df = DataFrame(item_details)

# for item in item_details:
#    # This does not give a very readable output
#    print(item)

# see the magic
print(items_df)
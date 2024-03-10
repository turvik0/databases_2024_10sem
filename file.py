from pymongo import MongoClient

client = MongoClient('mongodb://container_ip:27017')
db = client['my_data']
collection = db['my_collection']
#create
new_document = { "mykey": "myvalue" }
collection.insert_one(new_document)
#read
result = collection.find_one({"mykey": "myvalue"})
print(result)
#update
collection.update_one({ "key": "value" }, { "$set": { "newKey": "newValue" } })
#delete
collection.delete_one({ "key": "value" })
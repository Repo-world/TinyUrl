from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']
document = {"name": "John", "age": 30, "city": "New York"}
collection.insert_one(document)
found_document = collection.find_one({"name": "John"})
print(found_document)

client.close()

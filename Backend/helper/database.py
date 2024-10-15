import string
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['tinyUrlDatasets']


def storeUrl(longUrl, tinyUrl):
     document = {
          "tinyUrl":tinyUrl,
          "longUrl":longUrl
     }
     result = collection.insert_one(document)
     print(result)
     return str(result.inserted_id)

 # Return None in case of error
def getUrl(tinyUrl):
    try:
        result = collection.find_one({"tinyUrl": tinyUrl})
        return result['longUrl'] if result else None
    except Exception as e:
        
        return {"Exception in getting url from database ->" + str(e)}
   
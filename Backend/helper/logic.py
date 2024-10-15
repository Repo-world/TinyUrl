import random
import string
import hashlib
from helper.database import getUrl, storeUrl
def generateTinyUrl(longUrl,length=6):
    #before generating new random url check if its present inside the db
    try:
        result = getUrl(longUrl)
        if result:
            print("printint url "+result)
            return {"tinyUrl": result} 
    except Exception as e:
         return {"Error " : f"exception in fetching url "+str(e)} 
    try:
        value =  ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        tiny_url = f"http://tinyUrl.com/{value}"


        result = storeUrl(tiny_url, longUrl)
        if not result:
            raise Exception("Failed to store the new tiny URL.")
        
        return {"tinyUrl":tiny_url}
    
    except Exception as e:
        return {"Error": f"Failed in creating new url + str(e)"}


# def getUrl(tinyUrl):
#     return getUrl(tinyUrl)

# def generateTinyUrl(longUrl, length= 6):
#     m = hashlib.sha256()
#     m.update(longUrl.encode('utf-8'))
#     addition = (m.hexdigest()[:length])
#     tiny_url =f"https:tinyurl.com/{addition}"
#     return tiny_url


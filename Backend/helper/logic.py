import random
import string
import hashlib
from helper.database import storeUrl,getShortUrl
def generateTinyUrl(longUrl,length=6):
    #basically when the long url will come then i will remove the http/https part out of it,
    try:
        result = getShortUrl(longUrl)
        if result:
            return f'<a href="{result}">http://tinyUrl/{result}</a>'
    except Exception as e:
         return {"Error " : f"Exception in fetching url for first time: "+str(e)} 
    try:
        value =  ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        tiny_url = f"http://tinyUrl/{value}"

        result = storeUrl(value, longUrl)
        if not result:
            raise Exception("Failed to store the new tiny URL.")
        
        return f'<a href="{value}">{tiny_url}</a>'
    except Exception as e:
        return {"Error": f"Failed in creating new url + str(e)"}

def ensureProtocol(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        return "http://" + url
    return url

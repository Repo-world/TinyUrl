import random
import string
import hashlib
def generateTinyUrl(longUrl,length=6):
    value =  ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    tiny_url = f"http://tinyUrl.com/{value}"
    return tiny_url



# def generateTinyUrl(longUrl, length= 6):
#     m = hashlib.sha256()
#     m.update(longUrl.encode('utf-8'))
#     addition = (m.hexdigest()[:length])
#     tiny_url =f"https:tinyurl.com/{addition}"
#     return tiny_url


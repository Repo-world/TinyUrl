import random
import string
def generateTinyUrl(longUrl,length=6):
    value =  ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    tiny_url = f"http://tinyUrl.com/{value}"
    return tiny_url

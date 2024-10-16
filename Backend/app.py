from os import abort
from helper.database import getActualUrl
from flask import Flask, request, redirect
from helper.logic import generateTinyUrl, ensureProtocol

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world'  # Returning a simple string as a response

@app.route('/fetchUrl', methods=['GET'])
def getUrl():
    user_url = request.args.get('userUrl')
    if user_url:
        url_instance = generateTinyUrl(user_url)
        return url_instance , 200
    else:
        return "No user URL provided.", 400

@app.route('/<short_url>')
def getActualUrlLong(short_url):
    try:
        result = getActualUrl(short_url)
        if result:
            newUrl = ensureProtocol(result)
            print("result is " + newUrl)
            return redirect(newUrl)
        else:
            return abort(400)    # tiny url doesnot exist
    except Exception as e:
        return abort(500)     # server error

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from helper.logic import generateTinyUrl

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world'  # Returning a simple string as a response

@app.route('/fetchUrl', methods=['POST'])
def getUrl():
    user_url = request.args.get('userUrl')
    if user_url:
        url_instance = generateTinyUrl(user_url)
        return url_instance , 200
    else:
        return "No user URL provided.", 400

if __name__ == '__main__':
    app.run(debug=True)

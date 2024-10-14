from flask import Flask, render_template, request, redirect, url_for
from helper.databaseSetup import URL

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world'  # Returning a simple string as a response

@app.route('/fetchUrl', methods=['POST'])
def getUrl():
    
    user_url = request.args.get('userUrl')
    tiny_url = request.args.get('tinyUrl')
    up_time = request.args.get('upTime', default=0, type=int)
   
    if user_url:
        url_instance = URL(userUrl=user_url, tinyUrl=tiny_url, upTime=up_time)
        return f"Fetched URL: {url_instance.userUrl}, Tiny URL: {url_instance.tinyUrl}, Up Time: {url_instance.upTime} seconds"
    else:
        return "No user URL provided.", 400

if __name__ == '__main__':
    app.run(debug=True)
